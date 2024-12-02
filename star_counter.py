import cv2

def count_stars(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Unable to load the image.")
        return 0
    
    # Preprocess the image
    _, thresholded = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Count the number of contours (stars)
    star_count = len(contours)
    
    print(f"Number of stars detected: {star_count}")
    return star_count


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Count stars in an image.")
    parser.add_argument("image_path", help="Path to the input image.")
    args = parser.parse_args()
    
    count_stars(args.image_path)
