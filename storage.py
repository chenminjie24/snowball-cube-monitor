import json
import os
from typing import Dict, Optional


class Storage:
    """数据存储管理类，负责读写最新调仓记录ID"""
    
    def __init__(self, data_file: str = "data/last_rebalancing.json"):
        self.data_file = data_file
        self._ensure_data_dir()
    
    def _ensure_data_dir(self):
        """确保数据目录存在"""
        data_dir = os.path.dirname(self.data_file)
        if data_dir and not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def load_last_rebalancing_ids(self) -> Dict[str, int]:
        """
        加载最新调仓记录ID
        
        Returns:
            Dict[str, int]: 组合ID -> 最新调仓记录ID的映射
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"读取数据文件失败: {e}")
            return {}
    
    def save_last_rebalancing_ids(self, data: Dict[str, int]):
        """
        保存最新调仓记录ID
        
        Args:
            data: 组合ID -> 最新调仓记录ID的映射
        """
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"保存数据文件失败: {e}")
    
    def get_last_rebalancing_id(self, cube_id: str) -> Optional[int]:
        """
        获取指定组合的最新调仓记录ID
        
        Args:
            cube_id: 组合ID
            
        Returns:
            Optional[int]: 最新调仓记录ID，如果不存在则返回None
        """
        data = self.load_last_rebalancing_ids()
        return data.get(cube_id)
    
    def update_last_rebalancing_id(self, cube_id: str, rebalancing_id: int):
        """
        更新指定组合的最新调仓记录ID
        
        Args:
            cube_id: 组合ID
            rebalancing_id: 最新调仓记录ID
        """
        data = self.load_last_rebalancing_ids()
        data[cube_id] = rebalancing_id
        self.save_last_rebalancing_ids(data)
