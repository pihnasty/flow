from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# Пути к изображениям
image_paths = [
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\probability_loss_2025_06_28_07_44_31.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\probability_loss_2025_06_28_00_16_10.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\probability_loss_2025_06_28_01_04_52.jpeg",  # левая (красная)
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\probability_loss_2025_06_28_01_48_45.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\probability_loss_2025_06_28_02_17_35.jpeg",

    r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\probability_loss_2025_06_28_07_23_02.jpeg",
    r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\probability_loss_2025_06_28_07_44_31.jpeg",
]

# Пути к изображениям
# image_paths = [
#     r"C:\Users\pihna\Desktop\Новая папка\Paper\06_common_case\initial_data\risk_loss2025_06_28_00_16_14.jpeg",
#     r"C:\Users\pihna\Desktop\Новая папка\Paper\06_common_case\initial_data\risk_loss2025_06_28_01_04_55.jpeg",  # левая (красная)
#     r"C:\Users\pihna\Desktop\Новая папка\Paper\06_common_case\initial_data\risk_loss2025_06_28_01_48_49.jpeg",
#     r"C:\Users\pihna\Desktop\Новая папка\Paper\06_common_case\initial_data\risk_loss2025_06_28_02_17_36.jpeg",
#
#     r"C:\Users\pihna\Desktop\Новая папка\Paper\06_common_case\initial_data\risk_loss2025_06_28_07_23_03.jpeg",
#     r"C:\Users\pihna\Desktop\Новая папка\Paper\06_common_case\initial_data\risk_loss2025_06_28_07_44_32.jpeg",
# ]

# Пути к изображениям
# image_paths = [
#     r"C:\Users\pihna\Desktop\Новая папка\Paper\06_common_case\initial_data\risk_2025_06_28_00_16_07.jpeg",
#     r"C:\Users\pihna\Desktop\Новая папка\Paper\06_common_case\initial_data\risk_2025_06_28_01_04_47.jpeg",  # левая (красная)
#     r"C:\Users\pihna\Desktop\Новая папка\Paper\06_common_case\initial_data\risk_2025_06_28_01_48_39.jpeg",
#     r"C:\Users\pihna\Desktop\Новая папка\Paper\06_common_case\initial_data\risk_2025_06_28_02_17_34.jpeg",
#
#     r"C:\Users\pihna\Desktop\Новая папка\Paper\06_common_case\initial_data\risk_2025_06_28_07_23_00.jpeg",
#     r"C:\Users\pihna\Desktop\Новая папка\Paper\06_common_case\initial_data\risk_2025_06_28_07_44_29.jpeg",
# ]


# # Пути к изображениям
# image_paths = [
#     r"C:\A\Pro\flow\pom\pde\resultData\dataset\initial_data\probability_2025_06_28_02_17_33.jpeg",
#     r"C:\A\Pro\flow\pom\pde\resultData\dataset\initial_data\probability_2025_06_28_00_16_03.jpeg",  # левая (красная)
#     r"C:\A\Pro\flow\pom\pde\resultData\dataset\initial_data\probability_2025_06_28_01_04_44.jpeg",
#     r"C:\A\Pro\flow\pom\pde\resultData\dataset\initial_data\probability_2025_06_28_01_48_34.jpeg",
#
#     r"C:\A\Pro\flow\pom\pde\resultData\dataset\initial_data\probability_2025_06_28_07_22_59.jpeg",
#     r"C:\A\Pro\flow\pom\pde\resultData\dataset\initial_data\probability_2025_06_28_07_44_28.jpeg",
# ]

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
output_path = r"C:\A\Pro\flow\pom\pde\resultData\dataset\_initial_data\probability_loss_2025_06_28_left_black2.jpeg"

result_img.save(output_path, dpi=(1000, 1000))