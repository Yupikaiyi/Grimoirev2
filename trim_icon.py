from PIL import Image

def trim_aggressive(image_path, output_path, alpha_threshold=30):
    try:
        # We need to process the ORIGINAL image, not the one we already cropped, BUT
        # if we already saved over it, it's still 1492x1492 so we can still find the core.
        im = Image.open(image_path).convert("RGBA")
        
        # Create a boolean mask where alpha > threshold
        # point() applies a function to every pixel. For 'A' channel, this maps it to 255 or 0.
        alpha_mask = im.getchannel('A').point(lambda p: 255 if p > alpha_threshold else 0)
        
        # Get bounding box of the mask
        bbox = alpha_mask.getbbox()
        
        if bbox:
            print(f"Aggressive BBox (alpha > {alpha_threshold}):", bbox)
            # Crop the original image (with its glow preserved within the box, though truncated at the edges of the box)
            # Wait, truncating the glow hard might look weird if it's visible. 30 is a good balance.
            
            # Let's add a small padding of 5 pixels around the tight bounding box just so it's not cropped too harshly.
            pad = 10
            left = max(0, bbox[0] - pad)
            top = max(0, bbox[1] - pad)
            right = min(im.width, bbox[2] + pad)
            bottom = min(im.height, bbox[3] + pad)
            
            im_cropped = im.crop((left, top, right, bottom))
            
            # Make it a square
            max_dim = max(im_cropped.width, im_cropped.height)
            new_im = Image.new('RGBA', (max_dim, max_dim), (0, 0, 0, 0))
            offset_x = (max_dim - im_cropped.width) // 2
            offset_y = (max_dim - im_cropped.height) // 2
            new_im.paste(im_cropped, (offset_x, offset_y))
            
            new_im.save(output_path)
            print("Successfully cropped aggressively and centered.")
        else:
            print("No bounding box found for the given threshold.")
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    trim_aggressive("static/Icon.png", "static/Icon.png")
