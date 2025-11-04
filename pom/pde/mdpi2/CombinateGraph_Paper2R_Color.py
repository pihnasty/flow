from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# Пути к изображениям
image_paths = [
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\risk_per_detail2025_07_21_22_13_50.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\risk_per_detail2025_07_21_23_18_15.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\risk_per_detail2025_07_22_08_25_46.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\risk_per_detail2025_07_22_08_26_06.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\risk_per_detail2025_07_22_09_16_30.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\risk_per_detail2025_07_22_10_35_39.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\risk_per_detail2025_07_22_14_12_35.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\risk_per_detail2025_07_22_15_06_44.jpeg",


    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\risk_per_detail2025_07_21_17_00_53.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\risk_per_detail2025_07_21_17_56_39.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\risk_per_detail2025_07_21_19_14_36.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\risk_per_detail2025_07_21_19_39_58.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\risk_per_detail2025_07_21_20_08_57.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\risk_per_detail2025_07_21_20_34_19.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\risk_per_detail2025_07_21_21_01_29.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\risk_per_detail2025_07_21_21_42_58.jpeg",
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
    [255, 255, 0],    # желтый
    [0, 255, 255],    # бирюзовый (циан)
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
output_path = r"C:\A\Pro\flow\pom\pde\resultData\dataset\paper\rev2\f4d_risk2.jpeg"
result_img.save(output_path, dpi=(1000, 1000))
