from dataclasses import dataclass, field
from typing import Dict, Optional

@dataclass
class ProviderConfig:
    default_model: str
    base_url: Optional[str] = None

MODEL_CONFIGS: Dict[str, ProviderConfig] = {
    "deepseek": ProviderConfig(
        default_model="deepseek-v4-flash",
        base_url="https://deepseek.com"
    ),
    "qwen": ProviderConfig(
        default_model="qwen3.5-flash",
        base_url="https://aliyuncs.com"
    ),
    "openai": ProviderConfig(
        default_model="gpt-4o-mini",
        base_url=None  # openai library will automatically use https://openai.com
    )
}