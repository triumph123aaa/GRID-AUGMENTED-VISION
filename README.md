# GRID-AUGMENTED-VISION
## Introduction
Grid-Augmented Vision is a simple yet powerful approach to enhance spatial understanding in multi-modal AI systems. The project introduces a straightforward method of overlaying a 9×9 black grid pattern onto input images, which significantly improves the ability of AI models to precisely locate and map objects within images without requiring complex vision backbone architectures.
### Why Grid-Augmented Vision?
Traditional computer vision systems often struggle with precise spatial localization, particularly when converting conceptual object recognition into accurate coordinate mapping. While these systems excel at identifying objects, they frequently face challenges in determining exact locations. Our grid-based approach addresses this limitation by providing explicit spatial reference points that help models better understand and map spatial relationships.
### Implementation
The implementation of our approach focuses on simplicity and effectiveness. The grid generation process is implemented
through a straightforward algorithm that creates equally spaced horizontal and vertical lines across the image. The grid
is generated once for each input image and can be easily scaled to different image dimensions while maintaining the
9 × 9 structure.
Key implementation details include:
- Grid resolution: 9 × 9 fixed structure
- Line color: Black (#000000)
- Line transparency: 0.3 alpha value
- Line width: 1 pixel
- Integration method: Simple alpha blending
These design choices were derived from extensive experiments to ensure optimal performance in terms of balance
between visibility and minimal interference with the original image content.
The implementation methodology is illustrated in the following diagram：
<table>
  <tr>
    <td><img src="./figures/000000190756.jpg" width="400"></td>
    <td><img src="./figures/0000001907562.jpg" width="400"></td>
  </tr>
</table>

### Links
[![Paper](https://img.shields.io/badge/Paper-PDF-red)](https://arxiv.org/abs/2411.18270)

For a detailed exposition of our methodology, experimental results, and in-depth analysis, please refer to our paper.

## Quick Start
For a given raw image, it is first processed using `Writeline.py` to generate a grid-annotated image. Subsequently, after interaction with the large model, bounding box visualization is achieved through the `Visualization.py` script, enabling the graphical representation of object boundaries.

## Visualization
The specific usage process and the results of the visualization are illustrated in the following figure.

<div align="center">
  <img src="./figures/example.png" alt="Grid Implementation">
</div>

## Results
Our experimental results, as shown in Table 1, reveal several key findings:
 - Configuration Performance: The 9 × 9 black grid with 0.3 transparency demonstrated promising results,
 achieving an IoU of 0.56 and GIoU of 0.53, showing improvement over the baseline performance (IoU: 0.27,
 GIoU: 0.18) without grid overlay.
 - Grid Color Impact: Through our experiments, black grids tended to show better performance compared to
 white grids across various configurations. This might be attributed to the better contrast black grids provide
 against typical image contents.
 - Transparency Effects: The level of transparency appeared to influence localization accuracy. Moderate
 transparency (0.3) typically yielded better results compared to very transparent (0.1) or more opaque (0.5-1.0)
 settings, suggesting a potential trade-off between grid visibility and image content preservation.
<div align="center">
  <img src="./result/re.png" alt="Grid Implementation1">
</div>

## Citation
```bibtex
@article{chae2024grid,
  title={Grid-augumented vision: A simple yet effective approach for enhanced spatial understanding in multi-modal agents},
  author={Chae, Joongwon and Wang, Zhenyu and Qin, Peiwu},
  journal={arXiv preprint arXiv:2411.18270},
  year={2024}
}
```
