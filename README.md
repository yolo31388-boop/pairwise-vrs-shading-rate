# pairwise-vrs-shading-rate

## 领域

游戏、图形与多媒体

## 主题

可变速率着色

## 说明

按内容分块、运动矢量与 MSAA 兼容。

初始状态下 `render/vrs_shading_rate.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
