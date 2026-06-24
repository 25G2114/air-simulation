import numpy as np
import matplotlib.pyplot as plt

class Agent:
    """単一エージェントの定義"""
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=float)

    def move(self, step=0.5):
        # ランダム移動（上下左右 + 斜め）
        direction = np.random.uniform(-1, 1, size=2)
        self.position += direction * step


class Simulation:
    """エージェントシミュレーション環境"""
    def __init__(self, num_agents=20, area_size=10.0, proximity=1.5):
        if num_agents <= 0:
            raise ValueError("num_agents must be positive")
        if area_size <= 0:
            raise ValueError("area_size must be positive")

        self.area_size = float(area_size)
        self.proximity = float(proximity)

        # エージェントをランダム配置
        self.agents = [
            Agent(
                np.random.uniform(0, self.area_size),
                np.random.uniform(0, self.area_size),
            )
            for _ in range(num_agents)
        ]

    def step(self):
        """1 ステップ進める"""
        for ag in self.agents:
            ag.move()

            # エリア外に出たら反射
            ag.position = np.clip(ag.position, 0, self.area_size)

    def count_proximity_events(self):
        """一定距離以内のエージェントペア数を数える"""
        count = 0
        n = len(self.agents)
        for i in range(n):
            for j in range(i + 1, n):
                dist = np.linalg.norm(self.agents[i].position - self.agents[j].position)
                if dist < self.proximity:
                    count += 1
        return count

    def run(self, steps=50):
        """シミュレーションを実行"""
        if steps <= 0:
            raise ValueError("steps must be positive")

        proximity_log = []

        for _ in range(steps):
            self.step()
            proximity_log.append(self.count_proximity_events())

        return proximity_log


# 実行例（可視化あり）
if __name__ == "__main__":
    sim = Simulation(num_agents=30, area_size=20.0, proximity=1.5)
    log = sim.run(steps=100)

    # 可視化
    plt.plot(log)
    plt.title("Proximity Events Over Time")
    plt.xlabel("Step")
    plt.ylabel("Number of Events")
    plt.show()
