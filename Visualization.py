import cv2
import numpy as np

def visualize_bbox(image_path, bbox, color=(255, 0, 0), thickness=2):
    """
    Visualize a bounding box on an image
    
    Parameters:
    image_path (str): Path to the image file
    bbox (list): Bounding box coordinates in format [x1, y1, x2, y2]
    color (tuple): BGR color for the bounding box (default: green)
    thickness (int): Line thickness of the bounding box
    
    Returns:
    numpy.ndarray: Image with drawn bounding box
    """
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not read the image")
    
    # Convert bbox coordinates to integers
    x1, y1, x2, y2 = map(int, bbox)
    
    # Draw the rectangle
    image_with_box = cv2.rectangle(image.copy(), 
                                 (x1, y1), 
                                 (x2, y2), 
                                 color, 
                                 thickness)
    
    return image_with_box

def save_and_display(image, output_path):
    """
    Save the image and display it using cv2
    
    Parameters:
    image (numpy.ndarray): Image to save and display
    output_path (str): Path where to save the output image
    """
    # Save the image
    cv2.imwrite(output_path, image)
    
    # Display the image
    cv2.imshow('Image with Bounding Box', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
if __name__ == "__main__":
    # Example parameters
    image_path = r"C:\Users\lenovo\Desktop\dataimage\000000137246.jpg" # 替换为你的图片路径
    bbox = [150, 100, 350, 300]   # 替换为你的边界框坐标 [x1, y1, x2, y2]
    output_path = r"C:\Users\lenovo\Desktop\dataimage\000000137246output.jpg"  # 输出图片的保存路径
    
    # Visualize and save
    try:
        # Draw the bounding box
        image_with_bbox = visualize_bbox(image_path, bbox)
        
        # Save and display the result
        save_and_display(image_with_bbox, output_path)
        
        print(f"Result saved to {output_path}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
