from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# Пути к изображениям
image_paths = [
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_1_2_4_det_initial_data\risk_per_detail2025_07_21_13_32_28.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_1_2_4_det_initial_data\risk_per_detail2025_07_21_14_08_05.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_1_2_4_det_initial_data\risk_per_detail2025_07_21_14_45_09.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_1_2_4_det_initial_data\risk_per_detail2025_07_21_16_02_40.jpeg",



    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_1_2_4_risk_initial_data\risk_per_detail2025_07_21_10_04_42.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_1_2_4_risk_initial_data\risk_per_detail2025_07_21_10_33_21.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_1_2_4_risk_initial_data\risk_per_detail2025_07_21_11_01_24.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_1_2_4_risk_initial_data\risk_per_detail2025_07_21_16_34_34.jpeg",
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
output_path = r"C:\A\Pro\flow\pom\pde\resultData\dataset\paper\rev2\f4b_probability.jpeg"
result_img.save(output_path, dpi=(1000, 1000))
