from typing import Self, Optional

from glas.nodes.base import BaseNode


class SecondNode(BaseNode):
    def _execute(self, src: Self, dst: Self, task_id: str, args: dict[str, any] = None) -> tuple[int, Optional[str], Optional[str]]:
        if src.name == "Node one":        
            self.logger.info("Recieved package from Node one")
            return (0, self.id, "ok")
        
        return (1, self.id, "Unable to process SRC")