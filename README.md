# NewsAggregator

## Team:

-Mohamed Nguira (m.nguira@innopolis.university)

-Alsu Abdulmanova (a.abdulmanova@innopolis.university)

-Yakov Dementyev (y.dementyev@innopolis.university)


## Topic:
Develop an algorithm to search for duplicate news from Telegram channels with an indication of the subject of the news being evaluated. The task is to develop and train a model capable of efficiently identifying duplicate text fragments in large corpora of text information and classifying them into thematic groups. Create an algorithm designed to systematically identify duplicate news articles within Telegram channels, while also providing information about the specific subject matter of the news being assessed. The objective is to devise and train a model that can adeptly discern duplicate text segments within extensive collections of textual data, subsequently categorizing them into thematic groups. The ultimate goal is to enhance efficiency in recognizing and classifying duplicated content, particularly within the context of news articles disseminated through Telegram channels.

## Github link:
https://github.com/EveryoneHATEme/news_aggregator







## Data collection:

In the data collection phase, we employed a customized data parser to extract information from multiple Telegram channels. This sophisticated tool not only retrieved data but also underwent meticulous processing, with the labeled results available in the '/datasets' directory. The dataset was enriched by categorizing messages into 29 distinct categories, offering a comprehensive view of thematic diversity in the '/common' directory.

Our Telegram channel selection process was methodical, ensuring relevance to our investigative focus. Channels were chosen to represent diverse perspectives, enriching our dataset. The stories within these channels contribute to both the breadth and depth of insights derived from analyzing duplicated content across varied Telegram communities.






## Solution Building (Model Creation):

To address the challenge at hand, we opted for a two-model approach. The initial model involves a dual-input system, where two texts undergo a comparative analysis. Subsequently, the second model is responsible for text classification based on a single input.

In the first iteration, we employed the Universal Sentence Encoder to convert the input text into a 512-dimensional vector. The duplicate detection model utilized a Siamese architecture, where two Universal Sentence Encoders processed each text concurrently. The results were then combined and input into the full-link model, achieving an accuracy of 83%. For the classification model, we employed a CNN network that processed embeddings, resulting in an accuracy of 67%.

Our refined duplicate detection model employed an architecture sourced from the Sentence-Transformers library, utilizing the pre-trained model "distiluse-base-multilingual-cased-v1." Following fine-tuning, this model demonstrated an impressive accuracy of 99% on our dataset. Simultaneously, we fine-tuned the DistilBERT Multilingual model for classification purposes, achieving a satisfactory accuracy of 75% on our dataset.












## Main results (including artifacts):
### Duplicate model: 
Using SentenceTransformer: accuracy 0.998509, 10 epochs
These are results of the training for each epoch:


### Classification model:
DistilBERT: accuracy 0.779550, 3 epochs







Screenshot of working model using a telegram bot as an interface:











### Timeline of the project:

11 Sept - 18 Sept:
Finding and developing project idea

2 Oct - 9 Oct:
First model iteration
Parsing data
Preliminary results

22 Oct - 5 Nov:
Fine-tune model
Second model iteration

5 Nov - 28 Nov:
Finalizing the models
Developing Telegram bot
Results visualization
 
## Individual contributions of the teammates:
Yakov Dementyev - Team Lead, project idea, model developing, Telegram bot
Alsu Abdulmanova - data parse, fine-tune model, model developing
Mohamed Nguira - developing reports, data visualization, model testing

## References:
https://arxiv.org/pdf/1908.10084
https://towardsdatascience.com/building-a-news-aggregator-from-scratch-news-filtering-classification-grouping-in-threads-and-7b0bbf619b68
https://huggingface.co/blog/bert-101

