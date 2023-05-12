# 用户交互技术 - lab4

作者：2052526 白俊豪

时间：2023年5月12日12:09:28

链接: [Github](https://github.com/Rupert-WLLP-Bai/lab4-data-visualization)

- [用户交互技术 - lab4](#用户交互技术---lab4)
  - [项目简介](#项目简介)
  - [如何运行项目](#如何运行项目)
    - [建立虚拟环境](#建立虚拟环境)
    - [运行项目](#运行项目)
  - [项目依赖](#项目依赖)


## 项目简介

[Report.md](./docs/Report.md)

[Report-zh_CN.md](./docs/Report-zh_CN.md)

[Report.docx](./docs/Report.docx)

[Report-zh_CN.docx](./docs/Report-zh_CN.docx)

## 如何运行项目

### 建立虚拟环境

在下载本项目后，建议使用虚拟环境以避免与其他Python程序的依赖关系冲突。按照以下步骤建立虚拟环境：

1. 安装 Python 3.x。
2. 在项目根目录下，输入以下命令以创建一个新的虚拟环境：

```
python -m venv myenv
```

其中 `myenv` 可以改为你自己喜欢的名称。

1. 使用以下命令激活虚拟环境：

在 Unix 或 Linux 系统上：

```
source myenv/bin/activate
```

在 Windows 上：

```
.\myenv\Scripts\activate
```

### 运行项目

在虚拟环境中，运行以下命令以启动这个项目：

```
python app.py
```

等待控制台输出 "Running on http://127.0.0.1:8050/" 后，在浏览器中打开 http://127.0.0.1:8050/ 即可查看该项目的网页界面。

如果你想停止该项目，请使用Ctrl-C来退出服务。

## 项目依赖

本项目的依赖包括：

- `blinker==1.6.2`
- `click==8.1.3`
- `colorama==0.4.6`
- `dash==2.9.3`
- `dash-bootstrap-components==1.4.1`
- `dash-core-components==2.0.0`
- `dash-html-components==2.0.0`
- `dash-table==5.0.0`
- `Flask==2.3.2`
- `importlib-metadata==6.6.0`
- `itsdangerous==2.1.2`
- `Jinja2==3.1.2`
- `MarkupSafe==2.1.2`
- `numpy==1.24.3`
- `packaging==23.1`
- `pandas==2.0.1`
- `plotly==5.14.1`
- `python-dateutil==2.8.2`
- `pytz==2023.3`
- `six==1.16.0`
- `tenacity==8.2.2`
- `tzdata==2023.3`
- `Werkzeug==2.3.4`
- `zipp==3.15.0`

各个依赖的作用请参见各个依赖库的文档说明。