# services/timeline_service.py

import io

import matplotlib.pyplot as plt


class TimelineService:
    def __init__(self):
        self.colors = plt.cm.tab20c.colors
        self.timeline = [1250, 1650]
        self.lifetimes = {
            # ... Ваши данные ...
        }
        self.names = list(self.lifetimes.keys())

    def generate_timeline(self):
        fig, ax = plt.subplots()

        for i, (name, color) in enumerate(zip(self.names, self.colors)):
            start, end = self.lifetimes[name]
            ax.plot([start, end], [i, i], marker='o', color=color)
            ax.axvline(start, color='grey', linestyle='--', linewidth=0.5)
            ax.axvline(end, color='grey', linestyle='--', linewidth=0.5)

        ax.set_yticks(range(len(self.names)))
        ax.set_yticklabels(self.names)
        ax.set_xlim(self.timeline)
        ax.set_xlabel('Годы')
        ax.set_title('Временная шкала жизни известных персон')
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close(fig)  # Закрываем фигуру после сохранения в буфер
        return buf

    def f(self):
        return "timeline";
