const papersData = [
  {
    "title": "ObjectReact: Learning Object-Relative Control for Visual Navigation",
    "titleUrl": "https://object-react.github.io/",
    "authors": "Sourav Garg*, Dustin Craggs*, <strong>Vineeth Bhat</strong>, Lachlan Mares, Stefan Podgorski, Madhava Krishna, Feras Dayoub, Ian Reid",
    "venue": "CoRL",
    "year": "2025",
    "highlight": true,
    "categories": ["robotics"],
    "subtags": ["Robot learning", "Navigation"],
    "bibtex": "@inproceedings{garg2025objectreact,\n  title={ObjectReact: Learning Object-Relative Control for Visual Navigation},\n  author={Garg, Sourav and Craggs, Dustin and Bhat, Vineeth and Mares, Lachlan and Podgorski, Stefan and Krishna, Madhava and Dayoub, Feras and Reid, Ian},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2025}\n}",
    "links": [
      { "label": "project page", "url": "https://object-react.github.io/" },
      { "label": "arXiv", "url": "https://arxiv.org/abs/2509.09594" },
      { "label": "twitter", "url": "https://x.com/sourav_garg_/status/1966369557859467487f" }
    ],
    "description": "An object-relative control framework for visual navigation using a relative 3D scene graph, enabling more <i>flexible, embodiment-invariant path planning and control</i> that generalizes better across tasks and real-world environments than traditional image-relative methods.",
    "imageSrc": "images/objectreact/image.png",
    "videoSrc": "images/objectreact/video.mp4"
  },
  {
    "title": "SparseLoc: Sparse Open-Set Landmark-based Global Localization for Autonomous Navigation",
    "titleUrl": "https://reachpranjal.com/sparseloc/",
    "authors": "Pranjal Paul*, <strong>Vineeth Bhat*</strong>, Tejas Salian, Mohammad Omama, Krishna Murthy Jatavallabhula, Naveen Arulselvan, K. Madhava Krishna",
    "venue": "IROS",
    "year": "2025",
    "paperType": "Oral",
    "highlight": false,
    "categories": ["robotics"],
    "subtags": ["Localization"],
    "bibtex": "@inproceedings{paul2025sparseloc,\n  title={SparseLoc: Sparse Open-Set Landmark-based Global Localization for Autonomous Navigation},\n  author={Paul, Pranjal and Bhat, Vineeth and Salian, Tejas and Omama, Mohammad and Jatavallabhula, Krishna Murthy and Arulselvan, Naveen and Krishna, K. Madhava},\n  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},\n  year={2025}\n}",
    "links": [
      { "label": "project page", "url": "https://reachpranjal.com/sparseloc/" },
      { "label": "arXiv", "url": "https://arxiv.org/abs/2503.23465" }
    ],
    "description": "A global localization system that uses VLMs to build sparse, semantic maps. It achieves localization accuracy comparable to dense LiDAR methods <i>while using 500x fewer points</i>. Deployed in production by <a href=\"https://atimotors.com/\">Ati Motors</a>.",
    "imageSrc": "images/sparseloc/image.jpg",
    "videoSrc": "images/sparseloc/video.mp4"
  },
  {
    "title": "Consistency Checks for Language Model Forecasters",
    "titleUrl": "https://arxiv.org/abs/2412.18544",
    "authors": "Daniel Paleka*, Abhimanyu Pallavi Sudhir*, Alejandro Alvarez, <strong>Vineeth Bhat</strong>, Adam Shen, Evan Wang, Florian Tramèr",
    "venue": "ICLR",
    "year": "2025",
    "paperType": "Oral",
    "highlight": true,
    "categories": ["ai-safety"],
    "bibtex": "@inproceedings{paleka2025consistency,\n  title={Consistency Checks for Language Model Forecasters},\n  author={Paleka, Daniel and Sudhir, Abhimanyu Pallavi and Alvarez, Alejandro and Bhat, Vineeth and Shen, Adam and Wang, Evan and Tram\u00e8r, Florian},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2025}\n}",
    "links": [
      { "label": "arXiv", "url": "https://arxiv.org/abs/2412.18544" },
      { "label": "project code", "url": "https://github.com/dpaleka/consistency-forecasting" },
      { "label": "twitter", "url": "https://x.com/dpaleka/status/1877717539763237346" }
    ],
    "description": "Proposes a new framework for evaluating LLM-based forecasters by measuring their logical consistency, introducing an \"arbitrage metric\" that correlates strongly with future forecasting accuracy, even when the ground truth is unknown.",
    "imageSrc": "images/consistencychecks/image.png"
  },
  {
    "title": "Towards Global Localization Using Multi-Modal Object-Instance Re-Identification",
    "titleUrl": "https://instance-based-loc-machine.github.io/",
    "authors": "Aneesh Chavan, Vaibhav Agrawal*, <strong>Vineeth Bhat*</strong>, Sarthak Chittawar*, Siddharth Srivastava, Chetan Arora, K Madhava Krishna",
    "venue": "Advanced in Robotics",
    "year": "2025",
    "paperType": "Oral",
    "highlight": false,
    "categories": ["robotics"],
    "subtags": ["Localization"],
    "bibtex": "@inproceedings{chavan2025towards,\n  title={Towards Global Localization Using Multi-Modal Object-Instance Re-Identification},\n  author={Chavan, Aneesh and Agrawal, Vaibhav and Bhat, Vineeth and Chittawar, Sarthak and Srivastava, Siddharth and Arora, Chetan and Krishna, K. Madhava},\n  booktitle={Advances in Robotics (AiR)},\n  year={2025}\n}",
    "links": [
      { "label": "project page", "url": "https://instance-based-loc-machine.github.io/" },
      { "label": "arXiv", "url": "https://arxiv.org/abs/2409.12002" }
    ],
    "description": "A framework to build an object-based global map, and enables localization over it through a novel dual path transformer architecture that performs multi-modal instance re-identification.",
    "imageSrc": "images/dator/image.png"
  }
];
