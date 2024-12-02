def calculate_iou(box1, box2):
    """
    计算两个边界框的IoU
    参数:
        box1: [x1, y1, x2, y2] 格式的第一个边界框
        box2: [x1, y1, x2, y2] 格式的第二个边界框
    返回:
        iou: 两个框的IoU值
    """
    # 计算交集框的坐标
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    
    # 计算交集面积
    intersection = max(0, x2 - x1) * max(0, y2 - y1)
    
    # 计算各自面积
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    
    # 计算并集面积
    union = box1_area + box2_area - intersection
    
    # 计算IoU
    iou = intersection / union if union > 0 else 0
    
    return iou
def calculate_giou(box1, box2):
    """
    计算两个边界框的GIoU
    参数:
        box1: [x1, y1, x2, y2] 格式的第一个边界框
        box2: [x1, y1, x2, y2] 格式的第二个边界框
    返回:
        giou: 两个框的GIoU值
    """
    # 计算IoU
    iou = calculate_iou(box1, box2)
    
    # 计算最小闭包区域（包含两个框的最小框）的坐标
    c_x1 = min(box1[0], box2[0])
    c_y1 = min(box1[1], box2[1])
    c_x2 = max(box1[2], box2[2])
    c_y2 = max(box1[3], box2[3])
    
    # 计算最小闭包区域的面积
    c_area = (c_x2 - c_x1) * (c_y2 - c_y1)
    
    # 计算各自面积
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    
    # 计算并集面积
    union = box1_area + box2_area - (iou * (box1_area + box2_area - iou * box1_area * box2_area))
    
    # 计算GIoU
    giou = iou - ((c_area - union) / c_area)
    
    return giou
def calculate_diou(box1, box2):
    """
    计算两个边界框的DIoU
    参数:
        box1: [x1, y1, x2, y2] 格式的第一个边界框
        box2: [x1, y1, x2, y2] 格式的第二个边界框
    返回:
        diou: 两个框的DIoU值
    """
    # 计算IoU
    iou = calculate_iou(box1, box2)
    
    # 计算两个框中心点的距离
    center_x1 = (box1[0] + box1[2]) / 2
    center_y1 = (box1[1] + box1[3]) / 2
    center_x2 = (box2[0] + box2[2]) / 2
    center_y2 = (box2[1] + box2[3]) / 2
    
    center_distance = np.sqrt((center_x2 - center_x1)**2 + (center_y2 - center_y1)**2)
    
    # 计算最小闭包区域（包含两个框的最小框）的对角线距离
    c_x1 = min(box1[0], box2[0])
    c_y1 = min(box1[1], box2[1])
    c_x2 = max(box1[2], box2[2])
    c_y2 = max(box1[3], box2[3])
    
    diagonal_distance = np.sqrt((c_x2 - c_x1)**2 + (c_y2 - c_y1)**2)
    
    # 计算DIoU
    diou = iou - (center_distance**2) / (diagonal_distance**2)
    
    return diou
    
