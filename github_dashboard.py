import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns 

print("Starting Analysis")

# Load the dataset
st.header('Dataset Overview')
df = pd.read_csv('github_dataset.csv')

# Title of the dashboard
st.title('GitHub Repositories Analysis')

st.write('''
The GitHub Repositories Analysis Dashboard is an interactive tool built using Streamlit that provides insights into the activity, popularity, and collaboration patterns across GitHub repositories. It allows users to explore data related to stars, forks, issues, pull requests, contributors, and the programming languages used in various repositories. \nThe key features of the dashboard are:

1. Data Overview:\n
\tDisplays an overview of the dataset with the ability to filter data based on programming languages, issues, pull requests, and contributors.
\n\tUsers can interactively filter repositories using a sidebar, allowing them to focus on specific languages or repositories with certain ranges of stars, forks, issues, or contributors.
2. Visualizations:\n
\tDistribution of Stars and Forks:
Histograms provide a log-scaled view of how stars and forks are distributed across repositories, revealing the popularity skew.
\n\tTop Programming Languages:
A bar chart displays the top 10 programming languages based on the number of repositories, giving insights into the most popular languages in the dataset.
\n\tIssues and Pull Requests Analysis:
Histograms show the distribution of issues and pull requests, highlighting the variability in the number of issues reported and pull requests managed across repositories.
A scatter plot between issues and pull requests reveals the correlation between the two, identifying repositories with high engagement levels.
Tables display the top 10 repositories by issues and pull requests, helping users identify highly active projects.
\n3. Contributor Analysis:
\n\tDistribution of Contributors:
A histogram visualizes how contributors are distributed across repositories, showing whether community involvement is concentrated in a few projects or spread out.
\n\tTop Repositories by Number of Contributors:
Displays a table of repositories with the highest number of contributors, indicating highly collaborative and community-driven projects.
\n\tAverage Contributors per Programming Language:
A bar chart reveals the average number of contributors for the top programming languages, providing insights into which languages tend to have more collaborative repositories.
\n\tRelationship Between Contributors and Stars/Forks:
Scatter plots explore the relationship between the number of contributors and the stars or forks, identifying trends in how community size impacts popularity.
         ''')

# Display the data
st.header('Dataset Overview')
st.dataframe(df.head())

# Sidebar for filters
st.sidebar.header('Filters')
selected_language = st.sidebar.selectbox(
    'Select Language', 
    options=['All'] + list(df['language'].dropna().unique())
)
min_stars, max_stars = st.sidebar.slider(
    'Select Stars Range',
    min_value=int(df['stars_count'].min()),
    max_value=int(df['stars_count'].max()),
    value=(int(df['stars_count'].min()), int(df['stars_count'].max()))
)
min_forks, max_forks = st.sidebar.slider(
    'Select Forks Range',
    min_value=int(df['forks_count'].min()),
    max_value=int(df['forks_count'].max()),
    value=(int(df['forks_count'].min()), int(df['forks_count'].max()))
)
min_issues, max_issues = st.sidebar.slider(
    'Select Issues Range',
    min_value=int(df['issues_count'].min()),
    max_value=int(df['issues_count'].max()),
    value=(int(df['issues_count'].min()), int(df['issues_count'].max()))
)
min_prs, max_prs = st.sidebar.slider(
    'Select Pull Requests Range',
    min_value=int(df['pull_requests'].min()),
    max_value=int(df['pull_requests'].max()),
    value=(int(df['pull_requests'].min()), int(df['pull_requests'].max()))
)
min_contributors = st.sidebar.slider(
    'Minimum Number of Contributors',
    min_value=int(df['contributors'].min()),
    max_value=int(df['contributors'].max()),
    value=int(df['contributors'].min())
)

# Apply filters
filtered_df = df[
    (df['stars_count'] >= min_stars) & 
    (df['stars_count'] <= max_stars) &
    (df['forks_count'] >= min_forks) & 
    (df['forks_count'] <= max_forks) &
    (df['issues_count'] >= min_issues) & 
    (df['issues_count'] <= max_issues) &
    (df['pull_requests'] >= min_prs) & 
    (df['pull_requests'] <= max_prs) &
    (df['contributors'] >= min_contributors)
]
if selected_language != 'All':
    filtered_df = filtered_df[filtered_df['language'] == selected_language]

st.header(f'Repositories for {selected_language} (Filtered)')
st.dataframe(filtered_df)

# Summary statistics for the selected language
st.header('Summary Statistics')
st.write(filtered_df.describe())

# Distribution of Stars Count
st.header('Distribution of Stars Count')
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(filtered_df['stars_count'], bins=30, edgecolor='black')
ax.set_title('Distribution of Stars Count')
ax.set_xlabel('Stars Count')
ax.set_ylabel('Number of Repositories')
ax.set_yscale('log')  # Log scale for better visualization
st.pyplot(fig)

# Distribution of Forks Count
st.header('Distribution of Forks Count')
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(filtered_df['forks_count'], bins=30, edgecolor='black')
ax.set_title('Distribution of Forks Count')
ax.set_xlabel('Forks Count')
ax.set_ylabel('Number of Repositories')
ax.set_yscale('log')  # Log scale for better visualization
st.pyplot(fig)

# Distribution of Issues Count
st.header('Distribution of Issues Count')
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(filtered_df['issues_count'], bins=30, edgecolor='black')
ax.set_title('Distribution of Issues Count')
ax.set_xlabel('Issues Count')
ax.set_ylabel('Number of Repositories')
ax.set_yscale('log')  # Log scale for better visualization
st.pyplot(fig)

# Distribution of Pull Requests Count
st.header('Distribution of Pull Requests Count')
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(filtered_df['pull_requests'], bins=30, edgecolor='black')
ax.set_title('Distribution of Pull Requests Count')
ax.set_xlabel('Pull Requests Count')
ax.set_ylabel('Number of Repositories')
ax.set_yscale('log')  # Log scale for better visualization
st.pyplot(fig)

# Contributor-based Analysis: Distribution of Contributors
st.header('Distribution of Contributors Across Repositories')
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(filtered_df['contributors'], bins=30, edgecolor='black')
ax.set_title('Distribution of Contributors Across Repositories')
ax.set_xlabel('Number of Contributors')
ax.set_ylabel('Number of Repositories')
ax.set_yscale('log')  # Log scale for better visualization
st.pyplot(fig)

# Top 10 Programming Languages by Repository Count
st.header('Top 10 Programming Languages by Repository Count')
top_languages = df['language'].value_counts().nlargest(10)
fig, ax = plt.subplots(figsize=(10, 6))
top_languages.plot(kind='bar', ax=ax)
ax.set_title('Top 10 Programming Languages by Repository Count')
ax.set_xlabel('Programming Language')
ax.set_ylabel('Number of Repositories')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Scatter plot: Stars vs Forks
st.header('Stars vs. Forks')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=filtered_df, x='stars_count', y='forks_count', ax=ax)
ax.set_title('Stars vs. Forks')
ax.set_xlabel('Stars Count')
ax.set_ylabel('Forks Count')
ax.set_xscale('log')
ax.set_yscale('log')
st.pyplot(fig)

# Scatter plot: Issues vs Pull Requests
st.header('Issues vs. Pull Requests')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=filtered_df, x='issues_count', y='pull_requests', ax=ax)
ax.set_title('Issues vs. Pull Requests')
ax.set_xlabel('Issues Count')
ax.set_ylabel('Pull Requests Count')
ax.set_xscale('log')
ax.set_yscale('log')
st.pyplot(fig)

# Scatter plot: Contributors vs. Stars
st.header('Contributors vs. Stars')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=filtered_df, x='contributors', y='stars_count', ax=ax)
ax.set_title('Contributors vs. Stars')
ax.set_xlabel('Number of Contributors')
ax.set_ylabel('Stars Count')
ax.set_xscale('log')
ax.set_yscale('log')
st.pyplot(fig)

# Scatter plot: Contributors vs. Forks
st.header('Contributors vs. Forks')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=filtered_df, x='contributors', y='forks_count', ax=ax)
ax.set_title('Contributors vs. Forks')
ax.set_xlabel('Number of Contributors')
ax.set_ylabel('Forks Count')
ax.set_xscale('log')
ax.set_yscale('log')
st.pyplot(fig)

# Average stars and forks per language
st.header('Average Stars and Forks per Language')
avg_stars_forks = df.groupby('language')[['stars_count', 'forks_count']].mean().nlargest(10, 'stars_count')
fig, ax = plt.subplots(figsize=(10, 6))
avg_stars_forks.plot(kind='bar', ax=ax)
ax.set_title('Average Stars and Forks per Language')
ax.set_xlabel('Programming Language')
ax.set_ylabel('Average Count')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)


# Average issues and pull requests per language
st.header('Average Issues and Pull Requests per Language')
avg_issues_prs = df.groupby('language')[['issues_count', 'pull_requests']].mean().nlargest(10, 'issues_count')
fig, ax = plt.subplots(figsize=(10, 6))
avg_issues_prs.plot(kind='bar', ax=ax)
ax.set_title('Average Issues and Pull Requests per Language')
ax.set_xlabel('Programming Language')
ax.set_ylabel('Average Count')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Average Contributors per Programming Language
st.header('Average Contributors per Programming Language')
avg_contributors = df.groupby('language')['contributors'].mean().nlargest(10)
fig, ax = plt.subplots(figsize=(10, 6))
avg_contributors.plot(kind='bar', ax=ax)
ax.set_title('Average Contributors per Programming Language')
ax.set_xlabel('Programming Language')
ax.set_ylabel('Average Number of Contributors')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Top repositories by stars
st.header('Top Repositories by Stars')
top_issues_repos = df[['repositories', 'stars_count']].nlargest(10, 'stars_count')
st.table(top_issues_repos)

# Top repositories by forks
st.header('Top Repositories by Forks')
top_issues_repos = df[['repositories', 'forks_count']].nlargest(10, 'forks_count')
st.table(top_issues_repos)

# Top repositories by issues
st.header('Top Repositories by Issues')
top_issues_repos = df[['repositories', 'issues_count']].nlargest(10, 'issues_count')
st.table(top_issues_repos)

# Top repositories by pull requests
st.header('Top Repositories by Pull Requests')
top_prs_repos = df[['repositories', 'pull_requests']].nlargest(10, 'pull_requests')
st.table(top_prs_repos)

# Top Repositories by Number of Contributors
st.header('Top Repositories by Number of Contributors')
top_contributors_repos = df[['repositories', 'contributors']].nlargest(10, 'contributors')
st.table(top_contributors_repos)

# Heatmap of correlations
st.header('Correlation Heatmap')
corr = df[['stars_count', 'forks_count', 'issues_count', 'pull_requests', 'contributors']].corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Correlation Between Numeric Features')
st.pyplot(fig)

# Display the number of repositories by language in a pie chart
st.header('Repository Distribution by Language')
language_distribution = df['language'].value_counts()
fig, ax = plt.subplots()
language_distribution.plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=90)
ax.set_ylabel('')
st.pyplot(fig)
