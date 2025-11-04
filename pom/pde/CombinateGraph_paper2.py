from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# Пути к изображениям
image_paths = [
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\probability_per_detail2025_07_22_16_11_58.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\probability_per_detail2025_07_22_16_11_58.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\probability_per_detail2025_07_21_22_13_46.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\probability_per_detail2025_07_21_23_18_11.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\probability_per_detail2025_07_22_08_25_42.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\probability_per_detail2025_07_22_09_16_29.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\probability_per_detail2025_07_22_10_35_36.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\probability_per_detail2025_07_22_14_12_34.jpeg",
    # r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_22_8andMore_det_initial_data\probability_per_detail2025_07_22_15_06_41.jpeg",


    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\probability_per_detail2025_07_21_17_00_52.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\probability_per_detail2025_07_21_17_00_52.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\probability_per_detail2025_07_21_17_56_37.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\probability_per_detail2025_07_21_19_14_35.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\probability_per_detail2025_07_21_19_39_56.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\probability_per_detail2025_07_21_20_08_54.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\probability_per_detail2025_07_23_22_44_09.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\probability_per_detail2025_07_23_19_09_44.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\2025_07_21_8andMore_risk_initial_data\probability_per_detail2025_07_23_15_43_05.jpeg",

]

# Загружаем и приводим к одному размеру
images = [Image.open(path).convert('RGBA') for path in image_paths]
base_size = images[0].size
images = [img.resize(base_size) for img in images]

# Получаем numpy массивы RGBA
np_images = [np.array(img) for img in images]

# Маска линии левой кривой (image1):
# Предположим линии ярче фона, ищем яркие пиксели
gray_left = np.mean(np_images[0][:,:,:3], axis=2)  # средняя яркость RGB
mask_line_left = gray_left < 200  # порог, подкорректируй если надо (чем меньше — тем темнее, линия темная)

# Создаем RGB изображение для вывода (фон белый)
canvas = np.ones((base_size[1], base_size[0], 3), dtype=np.uint8) * 255

# Наносим левую кривую — красным цветом (оставляем остальные каналы)
# Копируем исходный rgb для левой картинки
left_rgb = np_images[0][:,:,:3].copy()

# Заменяем на красный там, где маска линии
left_rgb[mask_line_left] = [255, 0, 0]

# Наносим левую картинку на холст
canvas = left_rgb

# Теперь для остальных картинок добавим только линии (черным)
for img_arr in np_images[1:]:
    gray = np.mean(img_arr[:,:,:3], axis=2)
    mask_line = gray < 200  # порог для линий, подкорректируй при необходимости

    # Пиксели линии — черные
    canvas[mask_line] = [0, 0, 0]

# Показать результат
result_img = Image.fromarray(canvas)
plt.figure(figsize=(10,6))
plt.imshow(result_img)
plt.axis('off')
# plt.title("Left curve in red, others in black, axes untouched")
plt.show()

# Сохранение
output_path = r"C:\A\Pro\flow\pom\pde\resultData\dataset\paper\rev2\probability8andMore2.jpeg"

result_img.save(output_path, dpi=(1000, 1000))