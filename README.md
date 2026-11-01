# Semantic-Data-Technologies

Coursework and practical materials for Semantic Data Technologies (MOD004979).

## Week 3 NLP and SPARQL practicals

The self-contained [Week 3 folder](assignments/Week3_NLP_SPARQL/README.md) contains both bilingual notebooks, the source library dataset, required English NLP resources and portable launch configuration. The SPARQL notebook queries a real Fuseki `library` dataset and covers 19 tutorial examples plus 12 homework tasks.

On a new Windows x64 computer with Miniconda installed, double-click [environment/install-environment.bat](environment/install-environment.bat) once to prepare the software, update the ARU Python environment and register its Jupyter kernel. Then follow the assignment's run instructions.

## Hopfield sports ontology

The [Hopfield assignment](assignments/Hopfield_Sports_Ontology/) contains the group's v3.0 OWL ontology, the original question workbooks, 25 SPARQL queries and a script for generating RDFLib results, the group report and presentation, and Kangcheng Xu's individual work.

- [English assignment guide](assignments/Hopfield_Sports_Ontology/README.md) and [中文说明](assignments/Hopfield_Sports_Ontology/README.zh-CN.md)
- [Personal Jupyter notebook](assignments/Hopfield_Sports_Ontology/notebooks/Sports_Ontology_Xu_2623912.ipynb)
- [English four-slide presentation](assignments/Hopfield_Sports_Ontology/presentation/徐康成_体育本体_四页精简_英文版.pptx) and [Chinese presentation](assignments/Hopfield_Sports_Ontology/presentation/徐康成_体育本体_四页精简_中文版.pptx)

Open [Hopfield_Sports_Ontology.owl](assignments/Hopfield_Sports_Ontology/Hopfield_Sports_Ontology.owl) in Protégé, or run the notebook with the Python (ARU) kernel. The assignment folder includes the NLTK resources needed by the notebook. The individual data is a teaching sample; generated CSV files are asserted-graph query outputs, not reasoner or SHACL validation reports.

The group presentation still contains placeholder names and overlapping assignments. Check the final presentation with the group before submission.

## Windows environment

软件、安装恢复脚本和迁移说明集中在 [environment](environment/README.md)，包含 Protégé、Java 21、Fuseki 和 ARU Python/Jupyter 环境。另一台 Windows x64 电脑可按该说明恢复环境。

新电脑首次安装可直接阅读 [中文五步操作](environment/快速开始.md)。

## License

See [LICENSE](LICENSE). External reference sources remain subject to their respective terms.
