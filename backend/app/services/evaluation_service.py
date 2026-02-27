"""大模型输出评估服务"""

from typing import Dict, Any, Tuple
from .llm_service import get_llm


def evaluate_llm_accuracy(question: str, correct_answer: str, model: str = None) -> Dict[str, Any]:
    """
    评估大模型输出答案的正确率
    
    Args:
        question: 问题
        correct_answer: 正确答案
        model: 模型名称(可选)
        
    Returns:
        评估结果，包含模型答案、相似度得分和评估结论
    """
    try:
        # 获取LLM实例
        llm = get_llm()
        
        # 构建提示词
        messages = [{
            "role": "user",
            "content": f"问题: {question}\n\n请直接回答，不要添加任何额外的解释或引言。"
        }]
        
        # 调用LLM获取答案
        # 使用HelloAgentsLLM的invoke方法
        response = llm.invoke(messages)
        model_answer = response.content
        
        # 计算相似度得分
        similarity_score = calculate_similarity(model_answer, correct_answer)
        
        # 生成评估结论
        evaluation = generate_evaluation(similarity_score)
        
        # 构建评估结果
        result = {
            "question": question,
            "correct_answer": correct_answer,
            "model_answer": model_answer,
            "similarity_score": similarity_score,
            "evaluation": evaluation,
            "model": model or llm.model
        }
        
        return result
        
    except Exception as e:
        return {
            "error": str(e),
            "question": question,
            "correct_answer": correct_answer
        }


def calculate_similarity(text1: str, text2: str) -> float:
    """
    计算两个文本之间的相似度
    
    Args:
        text1: 第一个文本
        text2: 第二个文本
        
    Returns:
        相似度得分(0-1)
    """
    # 简单的相似度计算方法：基于共同词的比例
    # 实际应用中可以使用更复杂的方法，如余弦相似度、编辑距离等
    
    # 转换为小写并分词
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    
    # 计算共同词的数量
    common_words = words1.intersection(words2)
    
    # 计算相似度得分
    if len(words1) + len(words2) == 0:
        return 1.0
    
    similarity = len(common_words) / (len(words1) + len(words2) - len(common_words))
    return similarity


def generate_evaluation(score: float) -> str:
    """
    根据相似度得分生成评估结论
    
    Args:
        score: 相似度得分
        
    Returns:
        评估结论
    """
    if score >= 0.8:
        return "优秀：答案与正确答案高度一致"
    elif score >= 0.6:
        return "良好：答案与正确答案基本一致"
    elif score >= 0.4:
        return "一般：答案与正确答案部分一致"
    else:
        return "较差：答案与正确答案差异较大"


def evaluate_multiple_questions(questions: list) -> Dict[str, Any]:
    """
    批量评估多个问题的大模型回答
    
    Args:
        questions: 问题列表，每个元素为包含"question"和"correct_answer"的字典
        
    Returns:
        批量评估结果
    """
    results = []
    total_score = 0
    
    for item in questions:
        result = evaluate_llm_accuracy(
            item.get("question"),
            item.get("correct_answer")
        )
        results.append(result)
        if "similarity_score" in result:
            total_score += result["similarity_score"]
    
    # 计算平均得分
    average_score = total_score / len(questions) if questions else 0
    
    return {
        "results": results,
        "average_score": average_score,
        "overall_evaluation": generate_evaluation(average_score),
        "total_questions": len(questions)
    }
