	
<p align="center">
	<a href="https://postimg.cc/dL9WhCRB">
  		<img img src="https://i.postimg.cc/jdpBkQLG/ada-group-project-spaghetti-carbonada.png">
	</a>
</p>






<!-- [![ada-group-project-spaghetti-carbonada.png](https://i.postimg.cc/jdpBkQLG/ada-group-project-spaghetti-carbonada.png)](https://postimg.cc/dL9WhCRB) -->


# About YouNiverse
YouNiverse is a comprehensive dataset covering metadata from over 136,000 YouTube channels, 72.9 million videos, and 8.6 billion comments, offering valuable insights into platform dynamics, content trends, and user interactions.[Link](https://github.com/epfl-dlab/YouNiverse/tree/master)









# Framing our research


This study aims to explore the impact of the conspiracy theories proposed by Donald Trump on YouTube. Analyzing millions of videos, we reveal that conspiracy content drives higher engagement and trace how these narratives spread, often amplified by both mainstream and alternative channels. Our findings highlight how conspiracy theories become powerful tools for emotional engagement, illustrating YouTube’s role in amplifying political influence.





# What are we looking for? Research question


1. How did Trump use conspiracy theories to gain attention on YouTube? What is the trajectory of the dissemination of conspiracy theory-related content?
2. Do videos containing conspiracy theory content attract greater attention (e.g., likes, dislikes, views) compared to videos without conspiracy theory keywords?
3. Is there the trend of channels creating Trump-related videos with an entertainment focus generates higher view counts? And what are the subscription differences before and after a video publishing?
4. How do the presence of conspiracy theory keywords in the title or tags and whether the video belongs to the entertainment category interactively influence the number of likes a video receives?


# Initial exploration: what data do we have?

We have a dataset of 136,000 YouTube channels, 72.9 million videos, and 8.6 billion comments, offering valuable insights into platform dynamics, content trends, and user interactions.We filtered the data to include only videos related to Donald Trump. We split the data into two parts: with and without conspiracy theory keywords.

### Proportion of conspiracy theory videos in different categories
(task1)


### Tracing the Sequential Pathways of Trump-Related Conspiracy Theories on YouTube



### 1. Conspiracy Theory Distribution Map
{% include 3.1conspiracy_theory_distribution.html %}

### 2. Monthly Conspiracy Video Counts
{% include 3.2monthly_conspiracy_video_counts.html %}

### 3. Conspiracy Themes Frequency
{% include 3.3conspiracy_themes_frequency.html %}

### 4. Normalized Daily Conspiracy Video Counts
<iframe src="/_includes/3.4normalized_daily_conspiracy_video_counts.html" width="100%" height="600px" frameborder="0"></iframe>


### 5. Cross-Correlation of Conspiracy Categories
{% include 3.5cross_correlation_conspiracy_categories.html %}
