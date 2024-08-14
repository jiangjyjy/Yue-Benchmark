# CantoneseLM_survey 【三个链接+中文md】

[![evaluation](https://img.shields.io/badge/OpenCompass-Support-royalblue.svg
)](https://github.com/internLM/OpenCompass/) [![evaluation](https://img.shields.io/badge/lm--evaluation--harness-Support-blue
)](https://github.com/EleutherAI/lm-evaluation-harness)

<p align="center"> <img src="fig/banner.jpg" style="width: 100%;" id="title-icon">       </p>

<h4 align="center">
    <p>
        <a href="https://github.com/jiangjyjy/CantoneseLM_survey">简体中文</a> |
        <b>English</b> 
    <p>
</h4>

<p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center">
📄 <a href="https://arxiv.org/abs/xxxxx" target="_blank" style="margin-right: 15px; margin-left: 10px">Paper</a> • 
🏆 <a href="https://github.com/haonan-li/xxx" target="_blank"  style="margin-left: 10px">Leaderboard</a> •
🤗 <a href="https://huggingface.co/datasets/xxx" target="_blank" style="margin-left: 10px">Dataset</a> 
</p>

## Introduction

The Cantonese Benchmark is a new evaluation tool specifically designed for Cantonese, a language spoken by over 85 million people worldwide. As the field of natural language processing continues to grow, the need for robust evaluation tools tailored to specific languages becomes increasingly important. Addressing the significant gap in available benchmarks for Cantonese, this benchmark is composed of four distinct tasks (Cant-Truthful, Cant-GSM8K, Cant-ARC-C, Cant-MMLU), aiming to comprehensively evaluate the Cantonese capabilities of both Cantonese-specific and general-purpose large language models (LLMs) in the areas of factual generation, mathematical logic, complex reasoning, and general knowledge. By providing a reliable and accurate evaluation tool for Cantonese LLMs, the Cantonese Benchmark will not only facilitate the assessment of current models but also pave the way for future research and advancements in Cantonese natural language processing.


## Leaderboard

The following table displays the performance of models in the five-shot and zero-shot settings. 
<details>
<summary>Cant-TruthfulQA</summary>



|                       |      <th colspan=4>0-shot (correct)</th>                |                       |                       |                       | <th colspan=4>5-shot (correct)</th>                       |                       |                       |                       |
| ------------------------ | ------------ | ----------------- | -------------------- | ----------------- | -------------------- | ----------------- | -------------------- | ---------------- |
| Models  | Rouge-l   | Bleu-4 | BERTScore | Human  | Rouge-l   | Bleu-4 | BERTScore | Human |
| Qwen-1.5-110b                                        | 26.04                                          | 15.95                                         | 69.29              | --              | 31.73              | 19.53           | 70.87              | --              |
| Qwen-2-7b                                            | 13.27                                          | 10.00                                         | 66.14              | --              | 16.91              | 11.48           | 67.71              | --              |
| Qwen-2-72b                                           | 10.86                                          | 9.68                                          | 65.62              | --              | 17.52              | 12.38           | 67.72              | --              |
| Mixtral-8x22b                                        | 14.74                                          | 10.83                                         | 66.72              | --              | 20.40              | 14.09           | 68.05              | --              |
| Mixtral-large-2                                      | 19.72                                          | 13.01                                         | 69.06              | --              | 31.38              | 18.61           | 72.07              | --              |
| Llama-3-8b                                           | 8.40                                           | 8.68                                          | 64.37              | --              | 28.68              | 16.43           | 70.82              | --              |
| Llama-3-70b                                          | 10.98                                          | 9.51                                          | 66.10              | --              | 33.06              | 19.31           | 71.95              | --              |
| Llama-3.1-8b                                         | 13.82                                          | 10.33                                         | 66.97              | --              | 26.18              | 15.20           | 70.28              | --              |
| Llama-3.1-70b                                        | 21.03                                          | 14.30                                         | 68.31              | --              | 34.72              | 20.54           | 70.80              | --              |
| Phi-3-medium                                         | 18.70                                          | 12.00                                         | 67.36              | --              | 22.00              | 13.72           | 67.57              | --              |
| Gemma-2-27b                                          | 8.09                                           | 8.44                                          | 64.41              | --              | 11.33              | 9.98            | 63.66              | --              |
| Yi-1.5-34b                                           | 15.41                                          | 11.11                                         | 67.57              | --              | 20.30              | 13.20           | 69.50              | --              |
| Internlm-2.5-7b                                      | 14.46                                          | 10.53                                         | 63.48              | --              | 22.30              | 14.08           | 67.61              | --              |
| ERNIE-Lite                                           | 20.58                                          | 12.23                                         | 67.64              | --              | 20.69              | 12.27           | 68.45              | --              |
| ERNIE-Tiny                                           | 27.16                                          | 14.49                                         | 68.45              | --              | 27.91              | 15.28           | 68.84              | --              |
| ERNIE-Speed                                          | 22.58                                          | 13.15                                         | 67.84              | --              | 23.61              | 13.82           | 68.27              | --              |
| ERNIE-Turbo                                          | 17.91                                          | 11.30                                         | 66.71              | --              | 21.19              | 12.19           | 68.29              | --              |
| Sensechat-5                                          | 24.75                                          | 15.11                                         | 68.43              | --              | 32.45              | 19.70           | 70.02              | --              |
| Claude-3.5                                           | 14.23                                          | 9.95                                          | 67.56              | --              | 12.66              | 10.06           | 68.12              | --              |
| GLM-4                                                | 13.44                                          | 10.07                                         | 67.26              | --              | 23.57              | 14.28           | 70.30              | --              |
| ChatGPT                                              | 25.07                                          | 14.81                                         | 67.78              | --              | 31.84              | 18.42           | 70.41              | --              |
| GPT-4o                                               | 17.58                                          | 12.17                                         | 68.68              | --              | 27.64              | 16.52           | 71.59              | --              |
| GPT-4                                                | 19.47                                          | 13.45                                         | 68.99              | --              | 28.43              | 16.74           | 71.26              | --              |


</details>

<details>
<summary>Zero-shot</summary>

| Model               | STEM | Humanities | Social Science | Other | China-specific | Average |
|---------------------|------|------------|----------------|-------|----------------|---------|
| Open Access Models |
| [Qwen1.5-110B](https://modelscope.cn/models/qwen/Qwen1.5-110B)    | **80.84** | **91.51** | **89.01** | **89.99** | **88.64** | **87.64** |
| [Qwen2-72B](https://huggingface.co/Qwen/Qwen2-72B-Instruct)       |   80.92   |   90.90   |   87.93   |   91.23   |   87.24   |   87.47   |
| [PCI-TransGPT](http://123.249.36.167/call-frontend/#/transGpt)    |   76.69   |   86.26   |   81.71   |   84.47   |   83.13   |   82.44   |
| [Qwen1.5-72B](https://modelscope.cn/models/qwen/Qwen1.5-72B)      |   75.07   |   86.15   |   83.06   |   83.84   |   82.78   |   81.81   |
| [Qwen1.5-32B](https://modelscope.cn/models/qwen/Qwen1.5-32B)      |   74.82   |   85.13   |   82.49   |   84.34   |   82.47   |   81.47   |
| [BlueLM-7B](https://github.com/vivo-ai-lab/BlueLM)                |   62.08   |   81.29   |   79.38   |   79.56   |   77.69   |   75.40   |
| [Qwen1.5-7B](https://github.com/QwenLM/Qwen1.5)                   |   62.87   |   74.90   |   72.65   |   74.64   |   71.94   |   71.05   |
| [XuanYuan-70B](https://huggingface.co/Duxiaoman-DI/XuanYuan-70B)  |   61.21   |   76.25   |   74.44   |   70.67   |   69.35   |   70.59   |
| [Llama-3.1-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct)  |   61.60   |   71.44   |   69.42   |   74.72   |   63.79   |   69.01   |
| [GPT4](https://openai.com/gpt4)                                   |   63.16   |   69.19   |   70.26   |   73.16   |   63.47   |   68.90   |
| [Llama-3-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) |   57.02   |   67.87   |   68.67   |   73.95   |   62.96   |   66.74   |
| [XuanYuan-13B](https://github.com/Duxiaoman-DI/XuanYuan)          |   50.22   |  	67.55   |   63.85	|   61.17	|   61.50	|   60.51   |
| [Qwen-7B](https://github.com/QwenLM/Qwen-7B)                      |   46.33   |   62.54   |   60.48   |   61.72   |   58.77   |   57.57   |
| [ZhiLu-13B](https://github.com/SYSU-MUCFC-FinTech-Research-Center/ZhiLu)  |   43.53   |   61.60   |   61.40   |   60.15   |   58.97   |   57.14   |
| [ChatGPT](https://openai.com/chatgpt)                             |   44.80   |   53.61   |   54.22   |   59.95   |   49.74   |   53.22   |
| [Baichuan-13B](https://github.com/baichuan-inc/Baichuan-13B)      |   42.04   |   60.49   |   59.55   |   56.60   |   55.72   |   54.63   |
| [ChatGLM2-6B](https://huggingface.co/THUDM/chatglm2-6b)           |   41.28   |   52.85   |   53.37   |   52.24   |   50.58   |   49.95   |
| [BLOOMZ-7B](https://github.com/bigscience-workshop/xmtf)          |   33.03   |   45.74   |   45.74   |   46.25   |   41.58   |   42.80   |
| [Baichuan-7B](https://github.com/baichuan-inc/baichuan-7B)        |   32.79   |   44.43   |   46.78   |   44.79   |   43.11   |   42.33   |
| [ChatGLM-6B](https://github.com/THUDM/GLM-130B)                   |   32.22   |   42.91   |   44.81   |   42.60   |   41.93   |   40.79   |
| [BatGPT-15B](https://arxiv.org/abs/2307.00360)                    |   33.72   |   36.53   |   38.07   |   46.94   |   38.32   |   38.51   |
| [Falcon-40B](https://huggingface.co/tiiuae/falcon-40b)            |   31.11   |   41.30   |   40.87   |   40.61   |   36.05   |   38.50   |
| [LLaMA-65B](https://github.com/facebookresearch/llama)            |   31.09   |   34.45   |   36.05   |   37.94   |   32.89   |   34.88   |
| [Bactrian-LLaMA-13B](https://github.com/mbzuai-nlp/bactrian-x)    |   26.46   |   29.36   |   31.81   |   31.55   |   29.17   |   30.06   |
| [Chinese-LLaMA-13B](https://github.com/ymcui/Chinese-LLaMA-Alpaca)|   26.76   |   26.57   |   27.42   |   28.33   |   26.73   |   27.34   |
| [MOSS-SFT-16B](https://github.com/OpenLMLab/MOSS)                 |   25.68   |   26.35   |   27.21   |   27.92   |   26.70   |   26.88   |
| Models with Limited Access |
| [BlueLM]()                                                        | **76.36** | **90.34** | **86.23** | **86.94** | **86.84** | **84.68** |
| [DiMind]()                                                        | **70.92** | **86.66** | **86.04** | **86.60** | **81.49** | **82.73** |
| [云天天书]()                                                       |   73.03   |   83.78   |   82.30   |   84.04   |   81.37   |   80.62   |
| [Mind GPT]()                                                      |   71.20   |   83.95   |   80.59   |   82.11   |   78.90   |   79.20   |
| [QuarkLLM](https://www.quark.cn/)                                 |   67.23   |   81.69   |   79.47   |   80.74   |   77.00   |   77.08   |
| [Galaxy](https://www.zuoyebang.com/)                              |   69.38   |   75.33   |   78.27   |   78.19   |   73.25   |   73.85   |
| [ZW-LM]()                                                         |   63.93   |   77.95   |   76.28   |   72.99   |   72.94   |   72.74   |
| [KwaiYii-66B](https://github.com/kwai/KwaiYii)                    |   55.20   |   77.10   |   71.74   |   73.30   |   71.27   |   69.96   |
| [Mengzi-7B](https://www.langboat.com/)                            |   49.49   |   75.84   |   72.32   |   70.87   |   70.00   |   66.88   |
| [KwaiYii-13B](https://github.com/kwai/KwaiYii)                    |   46.82   |   69.35   |   63.42   |   64.02   |   63.26   |   61.22   |
| [MiLM-6B](https://github.com/XiaoMi/MiLM-6B/)                     |   48.88   |   63.49   |   66.20   |   62.14   |   62.07   |   60.37   |
| [MiLM-1.3B](https://github.com/XiaoMi/MiLM-6B/)                   |   40.51   |   54.82   |   54.15   |   53.99   |   52.26   |   50.79   |
| Random                                                            |   25.00   |   25.00   |   25.00   |   25.00   |   25.00   |   25.00   |
</details>





## Citation 【填词符】
```
xxxx
```

## License[证书存疑]

The CantoneseLM_survey dataset is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
