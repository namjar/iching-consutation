# 易经区块链迁移分析系统

基于易经原理的区块链创业迁移决策分析系统，结合传统智慧与现代技术，为区块链创业者提供迁移决策支持。

## 功能特点

- 卦象生成：根据用户输入主题随机生成卦象
- 多维分析：支持传统、商业、迁移等多种分析模板
- 五行分析：深入解读五行关系
- 智能建议：提供个性化迁移策略建议
- 跨平台支持：Web界面和iOS原生应用

## 技术栈

- 后端：Python 3.x + Flask
- 前端：HTML5 + Bootstrap 5 + JavaScript
- UI组件：Font Awesome + Axios
- iOS应用：Swift + UIKit
- 数据分析：NumPy + Pandas + Scikit-learn

## 快速开始

### Web应用

1. 克隆项目
```bash
git clone [项目地址]
cd iching
```

2. 创建虚拟环境（推荐）
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# 或
.\venv\Scripts\activate  # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 启动应用
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

访问 http://localhost:5000 即可使用系统。

### iOS应用

1. 安装依赖
```bash
cd ios_app
pod install
```

2. 使用 Xcode 打开 IChing.xcworkspace
3. 选择目标设备并运行

## 项目结构

```
iching/
├── app.py              # Flask应用主文件
├── main.py            # 主程序入口
├── requirements.txt    # Python依赖
├── Podfile            # iOS依赖
│
├── ai_analysis/       # AI分析模块
├── iching_core/       # 核心分析模块
│   ├── __init__.py
│   ├── five_elements.py
│   ├── hexagram_analyzer.py
│   ├── hexagram_generator.py
│   ├── relationship_analyzer.py
│   ├── time_calculator.py
│   └── trigrams.py
│
├── ios_app/           # iOS应用
│   ├── IChing/
│   └── IChing.xcodeproj/
│
├── models/           # 数据模型
│
├── static/           # Web静态资源
│   ├── css/         # 样式文件
│   └── js/          # JavaScript文件
│
└── templates/        # HTML模板
    ├── base.html    # 基础模板
    ├── index.html   # 主页
    └── result.html  # 结果页
```

## 开发指南

### Web开发
- 遵循 PEP 8 编码规范
- 使用模块化设计
- 保持代码简洁清晰
- 添加必要的注释

### iOS开发
- 遵循 Swift 编码规范
- 使用 MVVM 架构
- 支持深色模式
- 本地化支持

## 测试

```bash
# 运行Python测试
pytest

# 运行iOS测试
xcodebuild test -workspace ios_app/IChing.xcworkspace -scheme IChing -destination 'platform=iOS Simulator,name=iPhone 14'
```

## 许可证

MIT License

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目。

## 系统要求

- Python 3.8+
- iOS 14.0+
- macOS（用于iOS开发）