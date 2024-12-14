	
<p align="center">
	<a href="http://cdn.cnn.com/cnn/2020/images/07/17/csr_trumpconspiracies_fs_mon_9.jpg">
  		<img src="http://cdn.cnn.com/cnn/2020/images/07/17/csr_trumpconspiracies_fs_mon_9.jpg">
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

## Proportion of conspiracy theory videos in different categories
task1

{% include 1.1plotly_pie_chart.html %}


## 2
task2
The following CCDF plots illustrate the distributional discrepancies in key engagement metrics—namely view counts, like counts, dislike counts, and like–dislike ratios—between videos containing conspiracy-related keywords and those without such terminology. 
{% include 2.1plotly_view_count_comparison.html %}
{% include 2.2ccdf_like_dislike_side_by_side.html %}
{% include 2.3plotly_like_dislike_ratio_comparison.html %}
Utilizing non-parametric hypothesis testing procedures, specifically the Mann–Whitney U test, we decisively reject the null hypothesis at a significance level of α=0.01, illustrating that videos containing conspiracy-related keywords have significantly more views, likes, dislikes and higher like-dislike ration than those without conspiracy-related keywords.





## Tracing the Sequential Pathways of Trump-Related Conspiracy Theories on YouTube


### 1. Conspiracy Theory Distribution Map
{% include 3.1conspiracy_theory_distribution.html %}



### 2. Monthly Conspiracy Video Counts
{% include 3.2monthly_conspiracy_video_counts.html %}

A time-series analysis of these videos revealed two primary peaks in content volume: October 2018, coinciding with the U.S. midterm elections, and November 2019, aligning with the start of impeachment discussions. Given the significance of these periods, we focused our analysis on them.

### 3. Conspiracy Themes Frequency
{% include 3.3conspiracy_themes_frequency.html %}

From September to December 2019, mentions of the *Biden Family Scandal* surged in conspiracy content, driven by Trump’s focus on alleged Biden corruption amid the impeachment inquiry. Trump emphasized Hunter Biden’s Ukraine dealings to cast doubt on his political opponent and counter the impeachment narrative, fueling widespread conspiracy theories across media platforms.

From September to December 2018, "Deep State" and "QAnon" mentions spiked as Trump frequently referenced these conspiracies during the midterm election campaign. By highlighting the "Deep State," he sought to energize his base and frame opposition as part of a hidden government conspiracy, driving public interest and a surge of related content online.

### 4. Normalized Daily Conspiracy Video Counts
{% include 3.4.1normalized_daily_conspiracy_video_counts_Sep_Dec_2018.html %}
{% include 3.4.2normalized_daily_conspiracy_video_counts_Sep_Dec_2019.html %}

To analyze the features we want from the rather messy time series plots, we need to further perform correlation calculations, which means using the principle of convolution to find the temporal order.



### 5. Cross-Correlation of Conspiracy Categories
{% include 3.5cross_correlation_conspiracy_categories.html %}

The images show cross-correlation of normalized video counts, where a negative lag at peak correlation indicates that the second channel type released content earlier. This highlights the sequential release pattern across channel categories.

The results indicate that Trump-related conspiracy content first appears in the People & Blogs category, followed by News & Politics and Entertainment. This sequence is understandable, as People & Blogs videos generally require minimal editing or production, reflecting the public's immediate response. For example, someone might record a segment of a Trump interview on their phone and post it online instantly. News & Politics content follows closely behind, as news segments typically involve more preparation and editing, leading to a slightly delayed release. Entertainment videos are posted later as entertainment creators tend to process information from blogs or news and take additional time to consider how best to adapt the content for maximum engagement, often through added commentary or creative reinterpretation.
