import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

# 生成数据
x = np.linspace(0, 2*np.pi, 400)  # 从0到2π，生成400个点
y = np.sin(x)                     # 计算正弦值

# 创建图表
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')  # 蓝色实线
plt.xlabel('x (弧度)')
plt.ylabel('sin(x)')
plt.title('正弦函数图像')
plt.grid(True, alpha=0.3)
plt.legend()

# 标记特殊点
plt.plot(0, 0, 'ro', markersize=8)      # 原点
plt.plot(np.pi/2, 1, 'go', markersize=8) # 峰值点
plt.plot(np.pi, 0, 'ro', markersize=8)   # 过零点
plt.plot(3*np.pi/2, -1, 'go', markersize=8) # 谷值点

# 添加特殊点标注
plt.annotate('原点 (0, 0)', xy=(0, 0), xytext=(0.5, 0.3),
             arrowprops=dict(arrowstyle='->', color='red'))
plt.annotate('峰值 (π/2, 1)', xy=(np.pi/2, 1), xytext=(np.pi/2+0.5, 0.7),
             arrowprops=dict(arrowstyle='->', color='green'))
plt.annotate('谷值 (3π/2, -1)', xy=(3*np.pi/2, -1), xytext=(3*np.pi/2+0.5, -0.7),
             arrowprops=dict(arrowstyle='->', color='green'))

# 设置x轴范围和刻度
plt.xlim(-0.2, 2*np.pi + 0.2)
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], 
           ['0', 'π/2', 'π', '3π/2', '2π'])

# 显示图像
plt.tight_layout()
plt.savefig('D:/GitHub/Local-AI/data/sine_plot.png', dpi=300, bbox_inches='tight')
plt.show()

print("正弦函数图像已生成并保存为 'sine_plot.png'")

# 生成一个交互式的正弦函数可视化
from matplotlib.widgets import Slider, Button

# 创建交互式图表
fig, ax = plt.subplots(figsize=(12, 8))
plt.subplots_adjust(left=0.1, bottom=0.25)

# 初始参数
initial_amplitude = 1.0
initial_frequency = 1.0
initial_phase = 0.0

# 生成初始数据
x = np.linspace(0, 2*np.pi, 1000)
y = initial_amplitude * np.sin(initial_frequency * x + initial_phase)

# 绘制初始曲线
line, = ax.plot(x, y, 'b-', linewidth=2)
ax.set_xlabel('x (弧度)')
ax.set_ylabel('sin(x)')
ax.set_title('交互式正弦函数图像')
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-3, 3)

# 添加滑块控件
ax_amplitude = plt.axes([0.1, 0.15, 0.65, 0.03])
ax_frequency = plt.axes([0.1, 0.1, 0.65, 0.03])
ax_phase = plt.axes([0.1, 0.05, 0.65, 0.03])

slider_amplitude = Slider(ax_amplitude, '振幅 A', 0.1, 3.0, valinit=initial_amplitude)
slider_frequency = Slider(ax_frequency, '频率 ω', 0.1, 3.0, valinit=initial_frequency)
slider_phase = Slider(ax_phase, '相位 φ', 0, 2*np.pi, valinit=initial_phase)

# 更新函数
def update(val):
    amplitude = slider_amplitude.val
    frequency = slider_frequency.val
    phase = slider_phase.val
    
    y = amplitude * np.sin(frequency * x + phase)
    line.set_ydata(y)
    ax.set_ylim(-amplitude-0.5, amplitude+0.5)
    ax.set_title(f'正弦函数: y = {amplitude:.1f} × sin({frequency:.1f}x + {phase:.1f})')
    fig.canvas.draw_idle()

# 注册更新函数
slider_amplitude.on_changed(update)
slider_frequency.on_changed(update)
slider_phase.on_changed(update)

# 重置按钮
ax_reset = plt.axes([0.8, 0.025, 0.1, 0.04])
button_reset = Button(ax_reset, '重置', color='lightgoldenrodyellow', hovercolor='0.975')

def reset(event):
    slider_amplitude.reset()
    slider_frequency.reset()
    slider_phase.reset()

button_reset.on_clicked(reset)

plt.show()

print("交互式正弦函数可视化已启动！")

# 保存交互式图表为图片
plt.savefig('D:/GitHub/Local-AI/data/sine_plot_interactive.png', dpi=300, bbox_inches='tight')

# 生成多个正弦函数的比较
plt.figure(figsize=(12, 8))

x = np.linspace(0, 4*np.pi, 800)

# 绘制不同参数的正弦函数
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
plt.plot(x, np.sin(2*x), 'r-', linewidth=2, label='sin(2x)')
plt.plot(x, np.sin(3*x), 'g-', linewidth=2, label='sin(3x)')
plt.xlabel('x (弧度)')
plt.ylabel('sin(nx)')
plt.title('不同频率的正弦函数')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 2)
plt.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
plt.plot(x, 2*np.sin(x), 'r-', linewidth=2, label='2×sin(x)')
plt.plot(x, 0.5*np.sin(x), 'g-', linewidth=2, label='0.5×sin(x)')
plt.xlabel('x (弧度)')
plt.ylabel('A×sin(x)')
plt.title('不同振幅的正弦函数')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 3)
plt.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
plt.plot(x, np.sin(x + np.pi/4), 'r-', linewidth=2, label='sin(x + π/4)')
plt.plot(x, np.sin(x + np.pi/2), 'g-', linewidth=2, label='sin(x + π/2)')
plt.xlabel('x (弧度)')
plt.ylabel('sin(x + φ)')
plt.title('不同相位的正弦函数')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 4)
# 绘制复合函数
y1 = np.sin(x)
y2 = np.sin(2*x)
y3 = y1 + y2
plt.plot(x, y1, 'b--', linewidth=1, label='sin(x)')
plt.plot(x, y2, 'r--', linewidth=1, label='sin(2x)')
plt.plot(x, y3, 'k-', linewidth=2, label='sin(x) + sin(2x)')
plt.xlabel('x (弧度)')
plt.ylabel('y(x)')
plt.title('正弦函数叠加')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('D:/GitHub/Local-AI/data/sine_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("正弦函数比较图已生成并保存为 'sine_comparison.png'")

print("\n=== 正弦函数图像生成完成 ===")
print("生成的文件:")
print("1. sine_plot.png - 基本正弦函数图像")
print("2. sine_plot_interactive.png - 交互式可视化")
print("3. sine_comparison.png - 正弦函数比较图")
print("4. sine_plot.py - 完整的Python源代码")
