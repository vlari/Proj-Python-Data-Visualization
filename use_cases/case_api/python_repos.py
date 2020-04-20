import requests

from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')
response_api = r.json()

repo_dicts = response_api['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner}<br /> {description}'

    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"

    # Fill lists
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    labels.append(label)

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    }
}]

layout = {
    'title': 'Python projects on Github',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 24}
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 24}
    },
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='python_repos.html')
