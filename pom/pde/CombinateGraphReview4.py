from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# Пути к изображениям
image_paths = [
        r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\risk_2025_06_28_00_16_07.jpeg",
        r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\risk_2025_06_28_01_04_47.jpeg",
        r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\risk_2025_06_28_01_48_39.jpeg",
        r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\risk_2025_06_28_02_17_34.jpeg",

        r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\risk_2025_06_28_07_23_00.jpeg",
        r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\risk_2025_06_28_07_44_29.jpeg",
]

# Загружаем и приводим к одному размеру
images = [Image.open(path).convert('RGBA') for path in image_paths]
base_size = images[0].size
images = [img.resize(base_size) for img in images]

# Получаем numpy массивы RGBA
np_images = [np.array(img) for img in images]

# Создаем белый холст
canvas = np.ones((base_size[1], base_size[0], 3), dtype=np.uint8) * 255

# Задаем цвета для кривых (можно выбрать любые)
colors = [
    [255, 0, 0],      # красный
    [0, 0, 255],      # синий
    [0, 200, 0],      # зеленый
    [255, 165, 0],    # оранжевый
    [128, 0, 128],    # фиолетовый
    [0, 0, 0],        # черный
]

# Прорисовываем каждую кривую своим цветом
for idx, img_arr in enumerate(np_images):
    gray = np.mean(img_arr[:,:,:3], axis=2)
    mask_line = gray < 200  # условие для линии
    canvas[mask_line] = colors[idx % len(colors)]

# Показать результат
result_img = Image.fromarray(canvas)
plt.figure(figsize=(10,6))
plt.imshow(result_img)
plt.axis('off')
plt.show()

# Сохранение
output_path = r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\probability_loss_2025_06_28_colored4.jpeg"
result_img.save(output_path, dpi=(1000, 1000))
