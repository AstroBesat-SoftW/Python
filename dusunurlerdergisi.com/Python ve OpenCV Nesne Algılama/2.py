import cv2
import os
import numpy as np

def find_and_print_similarities(camera, image_folder):
    image_paths = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith(".jpg")]

    matched_images = set()  # Maintain a set of matched image names

    # Get the size of the frames from the camera
    ret, frame = camera.read()
    frame_height, frame_width, _ = frame.shape

    # Define the desired display width and height (you can adjust these values)
    display_width, display_height = 640, 480

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        # Resize the frame to the desired display size
        frame_resized = cv2.resize(frame, (display_width, display_height))

        # Convert the resized frame to grayscale for better matching
        frame_gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

        match_found = False

        for image_path in image_paths:
            template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Resize the template to match the size of the resized frame
            template_resized = cv2.resize(template, (display_width, display_height))

            # Perform template matching
            res = cv2.matchTemplate(frame_gray, template_resized, cv2.TM_CCOEFF_NORMED)
            threshold = 0.1  # You can adjust the threshold value as per your requirements
            loc = np.where(res >= threshold)

            for pt in zip(*loc[::-1]):
                match_found = True

                # Check if the image name has already been printed
                image_name = os.path.basename(image_path)
                if image_name not in matched_images:
                    # Print the name of the found image to the console
                    print("Bulundu:", image_name)
                    matched_images.add(image_name)

        if not match_found:
            print("Bulunamadı")

        cv2.imshow("Camera", frame_resized)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    url = "http://192.168.1.35:8080/video"  # Update with your IP camera URL
    camera = cv2.VideoCapture(url)
    image_folder = "images/"  # Update with your image folder path
    find_and_print_similarities(camera, image_folder)
