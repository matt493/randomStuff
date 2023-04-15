import time
from dataclasses import dataclass
import script
import utils

@dataclass()
class Engine:
	frameRate : int = 24
	running : bool = True

	def stop(self) -> bool:
		"""return True if engine is stopping, False otherwise"""
		self.running = False
		return not self.running


if __name__ == '__main__':
	script.start()		# called before the main loop
	while Engine.running:
		timeBefore = time.time()
		script.loop()
		timeAfter = time.time()

		timeDelta = timeAfter - timeBefore
		delay = ((1000.0 / Engine.frameRate) - timeDelta) / 1000.0
		# utils.log(f"delay={delay}\tdelta={timeDelta}")
		time.sleep(0 if delay < 0 else delay)
	script.stop()		# called right after the main loop

def initEngine() -> Engine:
	return Engine()