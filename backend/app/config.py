"""配置管理模块 - 安全版本"""

import os
from typing import List, Optional
from pydantic import BaseModel
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


class Settings(BaseModel):
    """应用设置"""
    # 应用信息
    app_name: str = "HelloAgents智能旅行助手"
    app_version: str = "1.0.0"
    
    # 服务器配置
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))
    
    # CORS配置
    cors_origins: str = os.getenv("CORS_ORIGINS", "http://localhost:5173,http://localhost:3000")
    
    # 日志级别
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
    # LLM配置
    llm_model_id: str = os.getenv("LLM_MODEL_ID", "qwen-turbo")
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    llm_base_url: str = os.getenv("LLM_BASE_URL", "")
    llm_timeout: int = int(os.getenv("LLM_TIMEOUT", "60"))
    
    # 高德地图API配置
    amap_api_key: str = os.getenv("AMAP_API_KEY", "")
    
    # Unsplash API配置
    unsplash_access_key: str = os.getenv("UNSPLASH_ACCESS_KEY", "")
    unsplash_secret_key: str = os.getenv("UNSPLASH_SECRET_KEY", "")
    
    def get_cors_origins_list(self) -> List[str]:
        """获取CORS允许的源列表"""
        return self.cors_origins.split(",")


def get_settings() -> Settings:
    """获取设置实例"""
    return Settings()


def validate_config() -> bool:
    """
    验证配置是否完整
    
    Returns:
        验证通过返回True，否则抛出ValueError
        
    Raises:
        ValueError: 当必要配置缺失时
    """
    settings = get_settings()
    errors = []
    
    # 验证LLM配置
    if not settings.llm_api_key:
        errors.append("LLM_API_KEY 未配置")
    if not settings.llm_base_url:
        errors.append("LLM_BASE_URL 未配置")
    
    # 验证高德地图API配置
    if not settings.amap_api_key:
        errors.append("AMAP_API_KEY 未配置")
    
    if errors:
        raise ValueError("\n".join(errors))
    
    return True


def print_config() -> None:
    """打印配置信息（隐藏敏感信息）"""
    settings = get_settings()
    
    print(f"应用名称: {settings.app_name}")
    print(f"版本: {settings.app_version}")
    print(f"服务器: {settings.host}:{settings.port}")
    
    # 隐藏敏感信息
    if settings.llm_api_key:
        print(f"LLM API Key: {settings.llm_api_key[:10]}...{settings.llm_api_key[-4:] if len(settings.llm_api_key) > 14 else ''}")
    else:
        print("LLM API Key: 未配置")
    
    print(f"LLM Base URL: {settings.llm_base_url}")
    print(f"LLM Model: {settings.llm_model_id}")
    print(f"日志级别: {settings.log_level}")
    
    # 高德地图API Key
    if settings.amap_api_key:
        print(f"高德地图API Key: {settings.amap_api_key[:10]}...{settings.amap_api_key[-4:] if len(settings.amap_api_key) > 14 else ''}")
    else:
        print("高德地图API Key: 未配置")


def get_safe_config() -> dict:
    """
    获取安全的配置信息（用于日志和调试）
    所有敏感信息都会被隐藏
    
    Returns:
        安全的配置字典
    """
    settings = get_settings()
    
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
        "host": settings.host,
        "port": settings.port,
        "log_level": settings.log_level,
        "llm_model_id": settings.llm_model_id,
        "llm_base_url": settings.llm_base_url,
        "llm_timeout": settings.llm_timeout,
        "llm_api_key": f"{settings.llm_api_key[:10]}...{settings.llm_api_key[-4:] if len(settings.llm_api_key) > 14 else '****'}" if settings.llm_api_key else "未配置",
        "amap_api_key": f"{settings.amap_api_key[:10]}...{settings.amap_api_key[-4:] if len(settings.amap_api_key) > 14 else '****'}" if settings.amap_api_key else "未配置",
        "cors_origins": settings.cors_origins_list
    }
