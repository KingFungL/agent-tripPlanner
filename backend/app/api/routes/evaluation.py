"""大模型评估API"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from pydantic import BaseModel
from ...services.evaluation_service import evaluate_llm_accuracy, evaluate_multiple_questions

router = APIRouter(prefix="/api/evaluation", tags=["evaluation"])


class EvaluationRequest(BaseModel):
    """评估请求模型"""
    question: str
    correct_answer: str
    model: str = None


class BatchEvaluationRequest(BaseModel):
    """批量评估请求模型"""
    questions: List[Dict[str, str]]


class EvaluationResponse(BaseModel):
    """评估响应模型"""
    success: bool
    message: str
    data: Dict[str, Any]


@router.post("/evaluate", response_model=EvaluationResponse)
async def evaluate(request: EvaluationRequest):
    """
    评估大模型输出答案的正确率
    
    Args:
        request: 评估请求
        
    Returns:
        评估结果
    """
    try:
        result = evaluate_llm_accuracy(
            request.question,
            request.correct_answer,
            request.model
        )
        
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
        
        return EvaluationResponse(
            success=True,
            message="评估完成",
            data=result
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/batch-evaluate", response_model=EvaluationResponse)
async def batch_evaluate(request: BatchEvaluationRequest):
    """
    批量评估大模型输出答案的正确率
    
    Args:
        request: 批量评估请求
        
    Returns:
        批量评估结果
    """
    try:
        result = evaluate_multiple_questions(request.questions)
        
        return EvaluationResponse(
            success=True,
            message="批量评估完成",
            data=result
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
