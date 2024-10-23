from typing import Self, Optional

from glas.nodes.base import BaseNode


class FirstNode(BaseNode):
    def _execute(self, src: Self, dst: Self, task_id: str, args: dict[str, any] = None) -> tuple[int, Optional[str], Optional[str]]:
        if dst.name == "Node two":
            self.logger.info("Sending package to Node two")
            return (0, self.id, "ok")
        
        return (1, self.id, "Unable to process DST")