import gifos

FONT_FILE_BITMAP = "./assets/fonts/JetBrainsMonoNerdFont-Regular.ttf"

def get_stats():
    ignore_repos = ['github-readme-stats', 'nixos-configs', 'pool']
    git_user_details = gifos.utils.fetch_github_stats("grosheth", ignore_repos)

    return git_user_details


def string_format(stats):
    for x, lang in enumerate(stats.languages_sorted):
        stats.languages_sorted[x] = list(stats.languages_sorted[x])
        stats.languages_sorted[x][0] = "{:<25}".format(lang[0])
        stats.languages_sorted[x][1] = "{:<5}".format(lang[1])
 
    stats.account_name = "{:<16}".format(stats.account_name) 
    stats.total_commits_all_time = "{:<10}".format(stats.total_commits_all_time)
    stats.total_pull_requests_made = "{:<6}".format(stats.total_pull_requests_made)
    stats.user_rank.level = "{:<9}".format(stats.user_rank.level)
    stats.user_rank.percentile = str(stats.user_rank.percentile) + " %"
    stats.user_rank.percentile = "{:<7}".format(stats.user_rank.percentile)

    return stats

def main():
    stats = get_stats()
    stats = string_format(stats)

    t = gifos.Terminal(1300, 1200, 15, 15, FONT_FILE_BITMAP, 15)
    t.set_font(FONT_FILE_BITMAP, 16, 0)
    t.toggle_show_cursor(False)

    monaLines0 = f"""
┌ CPU ─ 1.04 0.71 0.50 ────────────────────────────────────────────────────────────────────────────────────┐┌───────────────┐
│100%│                                                                                                     ││\x1b[36mCPU     Use    \x1b[0m│
│    │                                                                                                     ││               │
│    │                                                                                                     ││All            │
│    │                                                                                                     ││AVG     6%     │
│    │                                                                                                     ││\x1b[31mCPU0    5%\x1b[0m     │
│    │                                                                                                     ││\x1b[32mCPU1    8%\x1b[0m     │
│    │                                                                                                     ││\x1b[33mCPU2    5%\x1b[0m     │
│    │                                                                                                     ││\x1b[34mCPU3    6%\x1b[0m     │
│    │\x1b[31m                             ⣀⣀⠤⠤⠔⠒⠒⠤⠤⠤⣀⣀⡀                                                          \x1b[0m ││\x1b[35mCPU4    8%\x1b[0m     │
│    │\x1b[31m                   ⣀⣀⡠⠤⠤⠒⠒⠊⠉⠉            ⠈⠉⠉⠒⠒⠒⠤⠤⢄⣀⣀⡀                                               \x1b[0m ││\x1b[36mCPU5    3%\x1b[0m     │
│    │\x1b[31m         ⢀⣀⣀⠤⠤⠔⠒⠒⠉⠉                                 ⠈⠉⠉⠒⠒⠢⠤⠤⢄⣀⣀                                     \x1b[0m ││\x1b[37mCPU6    6%\x1b[0m     │
│    │\x1b[31m ⣀⡠⠤⠤⠒⠒⠉⠉⠁                 ⢀⣀⣀⣀⣀⡠⠤⠤⠤⠤⢄⣀⣀⣀⣀⣀⡀                   ⠉⣀⣀⣀⣀⣀⣀⣀⣀⡀⣀⣀⣀                        \x1b[0m ││\x1b[31mCPU7    6%\x1b[0m     │
│    │\x1b[32m   ⢀⣀⣀⣀⢀⣀⣀⣀⣀⠤⠤⠤⠤⠤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠒⠒⠒⠒⠒⠤⠤⠤⠤⠤⠤⣀⣀⣀⣀⣀⡀⠤⠤ \x1b[0m   ││\x1b[32mCPU8    3%\x1b[0m     │
│  0%│\x1b[33m⠒⠒⠒⠒⠒⠒⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠑⠒⠒ \x1b[0m   ││\x1b[33mCPU9    5%\x1b[0m     │
│    └─────────────────────────────────────────────────────────────────────────────────────────────────────││\x1b[34mCPU10   7%\x1b[0m     │
│  60s                                                                                                   0s││\x1b[35mCPU11   6%\x1b[0m     │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘└───────────────┘
┌ Memory ──────────────────────────────────────────────────────────────┐┌ Github Languages ─────────────────────────────────┐
│100%│                                     ┌──────────────────────────┐││\x1b[36m    Language▲                  usage%(t)           \x1b[0m│
│    │                                     │RAM: 15%   10.9GiB/62.7GiB│││                                                   │
│    │                                     │SWP:  0%   0.0GiB/8.8GiB  │││    {stats.languages_sorted[0][0]}   {stats.languages_sorted[0][1]} %            │
│    │                                     └──────────────────────────┘││    {stats.languages_sorted[1][0]}   {stats.languages_sorted[1][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[2][0]}   {stats.languages_sorted[2][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[3][0]}   {stats.languages_sorted[3][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[4][0]}   {stats.languages_sorted[4][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[5][0]}   {stats.languages_sorted[5][1]} %            │
│    │                                                                 ││                                                   │
│    │                                                                 │└───────────────────────────────────────────────────┘
│    │                                                                 │┌ Stats ────────────────────────────────────────────┐
│    │                                                                 ││\x1b[36m User          Commits    PRs   Rank   Percentile  \x1b[0m│
│    │                                                                 ││                                                   │
│    │                                                                 ││ {stats.account_name}{stats.total_commits_all_time}{stats.total_pull_requests_made}{stats.user_rank.level}{stats.user_rank.percentile}  │
│    │\x1b[33m⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒\x1b[0m││                                                   │
│  0%│\x1b[34m⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀\x1b[0m││                                                   │
│    └─────────────────────────────────────────────────────────────────││                                                   │
│  60s                                                               0s││                                                   │
└──────────────────────────────────────────────────────────────────────┘└───────────────────────────────────────────────────┘
┌ Network ────────────────────────────────────────────────────┐┌ Processes ─────────────────────────────────────────────────┐
│  1.2│                         ┌────────────────────────────┐││\x1b[36mPID(p)    Name(n)              CPU%(c)▼  Mem%(m)   R/s      \x1b[0m│
│     │                         │RX: 536.5Kb/s   All: 4.2GB  │││                                                            │
│     │                         │TX: 18.3Kb/s    All: 170.9MB│││2161      pipewire-pulse       0.1%      0.0%      0B/s     │
│     │                         └────────────────────────────┘││3899      brave                0.4%      0.5%      0B/s     │
│     │\x1b[33m⢣                               ⡠⡀                     \x1b[0m││240761    steamwebhelper       0.3%      0.4%      0B/s     │
│  0.8│\x1b[33m⠈⢆                             ⡰⠁⠱⡀                    \x1b[0m││240637    steamwebhelper       0.2%      0.3%      0B/s     │
│     │\x1b[33m ⠘⡄                           ⡰⠁  ⠱⡀                   \x1b[0m││197176    .kitty-wrapped       0.2%      1.3%      0B/s     │
│     │\x1b[33m  ⠱⡀          ⢀⣀⣀⣀           ⡜     ⠱⡀                ⣀⠤\x1b[0m││1473      X                    0.2%      0.3%      0B/s     │
│     │\x1b[33m   ⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁   ⠑⢄        ⡜       ⠱⡀          ⣀⠤⠔⠊⠉  \x1b[0m││25004     .spotify-wrapped     0.1%      0.6%      16KB/s   │
│  0.4│\x1b[33m                    ⠑⠤⡀   ⢀⠎         ⠱⡀     ⢀⠤⠒⠉       \x1b[0m││25190     .kitty-wrapped       0.1%      0.2%      0B/s     │
│     │\x1b[33m                      ⠈⠢⡀⢀⠎           ⠱⡀ ⣀⠔⠊⠁          \x1b[0m││25128     1.2.42.290 --no-san… 0.1%      0.5%      0B/s     │
│     │\x1b[33m                        ⠈⠊             ⠑⠉              \x1b[0m││240045    steam                0.1%      0.3%      0B/s     │
│     │\x1b[33m                                                       \x1b[0m││4235      brave                1.1%      0.8%      0B/s     │
│  0Mb│\x1b[35m⠒⠒⠤⠤⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠢⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠢⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤\x1b[0m││25228     zellij               0.0%      0.2%      0B/s     │
│     └───────────────────────────────────────────────────────││230964    nvim                 0.0%      0.1%      0B/s     │
│   60s                                                     0s││3864      brave                0.0%      0.8%      0B/s     │
└─────────────────────────────────────────────────────────────┘└────────────────────────────────────────────────────────────┘
    """

    monaLines1 = f"""
┌ CPU ─ 1.04 0.71 0.50 ────────────────────────────────────────────────────────────────────────────────────┐┌───────────────┐
│100%│                                                                                                     ││\x1b[36mCPU     Use    \x1b[0m│
│    │                                                                                                     ││               │
│    │                                                                                                     ││All            │
│    │                                                                                                     ││AVG     9%     │
│    │                                                                                                     ││\x1b[31mCPU0    5%\x1b[0m     │
│    │                                                                                                     ││\x1b[32mCPU1    8%\x1b[0m     │
│    │                                                                                                     ││\x1b[33mCPU2    12%\x1b[0m    │
│    │                                                                                                     ││\x1b[34mCPU3    8%\x1b[0m     │
│    │\x1b[31m                                              ⢀                                                      \x1b[0m││\x1b[35mCPU4    9%\x1b[0m     │
│    │\x1b[31m                                           ⣀⢀⡠⠔⠤⣀⢄                       ⣀⡀                          \x1b[0m││\x1b[36mCPU5    4%\x1b[0m     │
│    │\x1b[31m                                        ⣀⣀⠔⠊⠁⠤⠒⠢⢄⠉⠒⠤⣀                ⣀⠤⠒⠉⣀⣀⡀⠑⠒⠢⠤⢄⣀⡀⣀                 \x1b[0m││\x1b[37mCPU6    10%\x1b[0m    │
│    │\x1b[35m                                     ⢀⠤⠒⠉⠒⠊⢀⣀⡠⠤⠤⣀⣀⠉⠒⠢⠉⠒⠤⣀        ⣀⠤⢀⣀⡠⠤⠒⠒⠉⠉⠉⠒⠒⠒⠒⠢⠤⠤⠤⠤⣀⣀⣀⣀⡀⣀⡀⣀⣀⣀⡀⣀⣀⣀⡀⡀\x1b[0m││\x1b[31mCPU7    7%\x1b[0m     │
│    │\x1b[34m⣀⣀⣀⢀⣀⣀⣀⣀⣀⣀⢀⢀⣀⡠⠤⠤⠒⠒⠉⠉⠁⠉⠁⣀⣀⠉⠉⠉⠉⠑⠒⠢⠤⠤⣀⣀⠤⣀⣀⣀⠤⠔⠒⠉⠉⠉⠉⠁⠉          ⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠑⠒⠒⠢⠤⠤⠤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⣀⣀⣀⣀⣀⣀\x1b[0m││\x1b[32mCPU8    8%\x1b[0m     │
│  0%│\x1b[33m⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠉⠉⠉⠉⠉⠉⠉⠉⠁⠉⠉⠉⠉⠉⠉⠉⠉⠁⠉⠉⠉⠉⠉⠉⠉⠉⠁⠉⠁⠉⠉⠉⠉⠉⠉⠉⠁\x1b[0m││\x1b[33mCPU9    2%\x1b[0m     │
│    └─────────────────────────────────────────────────────────────────────────────────────────────────────││\x1b[34mCPU10   4%\x1b[0m     │
│  60s                                                                                                   0s││\x1b[35mCPU11   6%\x1b[0m     │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘└───────────────┘
┌ Memory ──────────────────────────────────────────────────────────────┐┌ Github Languages ─────────────────────────────────┐
│100%│                                     ┌──────────────────────────┐││\x1b[36m    Language▲                  usage%(t)\x1b[0m           │
│    │                                     │RAM: 16%   10.9GiB/62.7GiB│││                                                   │
│    │                                     │SWP:  0%   0.0GiB/8.8GiB  │││    {stats.languages_sorted[0][0]}   {stats.languages_sorted[0][1]} %            │                         
│    │                                     └──────────────────────────┘││    {stats.languages_sorted[1][0]}   {stats.languages_sorted[1][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[2][0]}   {stats.languages_sorted[2][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[3][0]}   {stats.languages_sorted[3][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[4][0]}   {stats.languages_sorted[4][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[5][0]}   {stats.languages_sorted[5][1]} %            │
│    │                                                                 ││                                                   │
│    │                                                                 │└───────────────────────────────────────────────────┘
│    │                                                                 │┌ Stats ────────────────────────────────────────────┐
│    │                                                                 ││\x1b[36m User          Commits    PRs   Rank   Percentile  \x1b[0m│                                                                             nt(t) \x1b[0m│
│    │                                                                 ││                                                   │
│    │                                                                 ││ {stats.account_name}{stats.total_commits_all_time}{stats.total_pull_requests_made}{stats.user_rank.level}{stats.user_rank.percentile}  │
│    │\x1b[33m⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒\x1b[0m││                                                   │
│  0%│\x1b[34m⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀\x1b[0m││                                                   │
│    └─────────────────────────────────────────────────────────────────││                                                   │
│  60s                                                               0s││                                                   │
└──────────────────────────────────────────────────────────────────────┘└───────────────────────────────────────────────────┘
┌ Network ────────────────────────────────────────────────────┐┌ Processes ─────────────────────────────────────────────────┐
│  1.2│                         ┌────────────────────────────┐││\x1b[36mPID(p)    Name(n)              CPU%(c)▼  Mem%(m)   R/s      \x1b[0m│
│     │                         │RX: 536.5Kb/s   All: 4.2GB  │││                                                            │
│     │                         │TX: 18.3Kb/s    All: 170.9MB│││4235      brave                1.1%      0.8%      0B/s     │
│     │                         └────────────────────────────┘││3899      brave                0.4%      0.5%      0B/s     │
│     │\x1b[33m       ⡠⡀                                            \x1b[0m  ││240761    steamwebhelper       0.3%      0.4%      0B/s     │
│  0.8│\x1b[33m      ⡰⠁⠱⡀                                            \x1b[0m ││1473      X                    0.2%      0.3%      0B/s     │
│     │\x1b[33m     ⡰⠁  ⠱⡀                                           \x1b[0m ││197176    .kitty-wrapped       0.2%      1.3%      0B/s     │
│     │\x1b[33m    ⡜     ⠱⡀                ⣀⠤⡀          ⢀⣀⣀⣀         \x1b[0m ││240637    steamwebhelper       0.2%      0.3%      0B/s     │
│     │\x1b[33m    ⡜       ⠱⡀          ⣀⠤⠔⠊⠉  ⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁   ⠑⢄      \x1b[0m ││25004     .spotify-wrapped     0.1%      0.6%      16KB/s   │
│  0.4│\x1b[33m  ⢀⠎         ⠱⡀     ⢀⠤⠒⠉                        ⠑⠤⡀    \x1b[0m││25190     .kitty-wrapped       0.1%      0.2%      0B/s     │
│     │\x1b[33m ⢀⠎           ⠱⡀ ⣀⠔⠊⠁                             ⠈⠢⡀  \x1b[0m││25128     1.2.42.290 --no-san… 0.1%      0.5%      0B/s     │
│     │\x1b[33m ⠊             ⠑⠉                                   ⠈  \x1b[0m││240045    steam                0.1%      0.3%      0B/s     │
│     │\x1b[33m                                                       \x1b[0m││2161      pipewire-pulse       0.1%      0.0%      0B/s     │
│  0Mb│\x1b[35m⠒⠒⠤⠤⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠢⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠢⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤\x1b[0m││25228     zellij               0.0%      0.2%      0B/s     │
│     └───────────────────────────────────────────────────────││230964    nvim                 0.0%      0.1%      0B/s     │
│   60s                                                     0s││3864      brave                0.0%      0.8%      0B/s     │
└─────────────────────────────────────────────────────────────┘└────────────────────────────────────────────────────────────┘
    """

    monaLines2 = f"""
┌ CPU ─ 1.04 0.71 0.50 ────────────────────────────────────────────────────────────────────────────────────┐┌───────────────┐
│100%│                                                                                                     ││\x1b[36mCPU     Use    \x1b[0m│
│    │                                                                                                     ││               │
│    │                                                                                                     ││All            │
│    │                                                                                                     ││AVG     3%     │
│    │                                                                                                     ││\x1b[31mCPU0    1%     \x1b[0m│
│    │                                                                                                     ││\x1b[32mCPU1    8%     \x1b[0m│
│    │                                                                                                     ││\x1b[33mCPU2    8%     \x1b[0m│
│    │                                                                                                     ││\x1b[34mCPU3    13%    \x1b[0m│
│    │                                                                                                     ││\x1b[35mCPU4    9%     \x1b[0m│
│    │                                                                                                     ││\x1b[36mCPU5    10%    \x1b[0m│
│    │\x1b[34m⣀                                                                        ⣀⡀                          \x1b[0m││\x1b[37mCPU6    10%    \x1b[0m│
│    │\x1b[37m⣀             ⢀⣀⡠⠤⣀    ⣀⠤⣀    ⢀⣀     ⣀⠤⣀⡀          ⣀⣀⣀⣀⣀⣀⣀⣀⣀    ⣀⠤⠒⠤⠤⣀⡀        ⢀⣀      ⣀    ⣀⡠⠤⣀     \x1b[0m││\x1b[31mCPU7    7%     \x1b[0m│
│    │\x1b[32m⣀⣀⣤⡴⠶⢖⣒⣒⠤⠤⠤⠤⠒⠒⠉⠁    ⣀⠤⠒⠉   ⠉⠒⠢⢄⡀⣀⢀⣀⣀⠤⠤⠒⠒⠢⠤⠤⣀⣀⢄⣀⣀⠒⠒⠉⠉     ⣀⣀⣀⣀⣀⠤⠒⠉⢀⣀⣀⡀  ⣈⣉⣑⣒⣤⠤⣀⡀⠊⠁ ⠉⠒⣀⠤⠒⠉⣀⠉⠑⠒⠤⣀⡀  ⠉⠑⠒⠤\x1b[0m││\x1b[32mCPU8    3%     \x1b[0m│
│  0%│\x1b[31m⣀⠒⠒⠉⠉⠉⠉⠉⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠉⠉⠉⠉⠉⠉⠉⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠉⠉⠉⠉⠉⠉⠉⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒\x1b[0m││\x1b[33mCPU9    2%     \x1b[0m│
│    └─────────────────────────────────────────────────────────────────────────────────────────────────────││\x1b[34mCPU10   4%     \x1b[0m│
│  60s                                                                                                   0s││\x1b[35mCPU11   6%     \x1b[0m│
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘└───────────────┘
┌ Memory ──────────────────────────────────────────────────────────────┐┌ Github Languages ─────────────────────────────────┐
│100%│                                     ┌──────────────────────────┐││\x1b[36m    Language▲                  usage%(t)           \x1b[0m│                                                       t)    \x1b[0m│
│    │                                     │RAM: 17%   10.9GiB/62.7GiB│││                                                   │
│    │                                     │SWP:  0%   0.0GiB/8.8GiB  │││    {stats.languages_sorted[0][0]}   {stats.languages_sorted[0][1]} %            │
│    │                                     └──────────────────────────┘││    {stats.languages_sorted[1][0]}   {stats.languages_sorted[1][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[2][0]}   {stats.languages_sorted[2][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[3][0]}   {stats.languages_sorted[3][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[4][0]}   {stats.languages_sorted[4][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[5][0]}   {stats.languages_sorted[5][1]} %            │
│    │                                                                 ││                                                   │
│    │                                                                 │└───────────────────────────────────────────────────┘
│    │                                                                 │┌ Stats ────────────────────────────────────────────┐
│    │                                                                 ││\x1b[36m User          Commits    PRs   Rank   Percentile  \x1b[0m│
│    │                                                                 ││                                                   │
│    │                                                                 ││ {stats.account_name}{stats.total_commits_all_time}{stats.total_pull_requests_made}{stats.user_rank.level}{stats.user_rank.percentile}  │
│    │\x1b[33m⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒\x1b[0m││                                                   │
│  0%│\x1b[34m⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀\x1b[0m││                                                   │
│    └─────────────────────────────────────────────────────────────────││                                                   │
│  60s                                                               0s││                                                   │
└──────────────────────────────────────────────────────────────────────┘└───────────────────────────────────────────────────┘
┌ Network ────────────────────────────────────────────────────┐┌ Processes ─────────────────────────────────────────────────┐
│  1.2│                         ┌────────────────────────────┐││\x1b[36mPID(p)    Name(n)              CPU%(c)▼  Mem%(m)   R/s      \x1b[0m│
│     │                         │RX: 536.5Kb/s   All: 4.2GB  │││                                                            │
│     │                         │TX: 18.3Kb/s    All: 170.9MB│││4235      brave                1.1%      0.8%      0B/s     │
│     │                         └────────────────────────────┘││3899      brave                0.4%      0.5%      0B/s     │
│     │                                                       ││240761    steamwebhelper       0.3%      0.4%      0B/s     │
│  0.8│                                                       ││230964    nvim                 0.0%      0.1%      0B/s     │
│     │                                                       ││197176    .kitty-wrapped       0.2%      1.3%      0B/s     │
│     │                                                       ││2161      pipewire-pulse       0.1%      0.0%      0B/s     │
│     │ \x1b[33m⢠                                      ⢠⢣          ⡇⠸⡇\x1b[0m││25004     .spotify-wrapped     0.1%      0.6%      16KB/s   │
│  0.4│\x1b[33m⢀⢀⢣                                    ⢀⠇⠈⢆        ⡸⠃ ⠸\x1b[0m││25190     .kitty-wrapped       0.1%      0.2%      0B/s     │
│     │\x1b[33m⢀⠎⢣⢣                                   ⡜\x1b[35m⠜⠘⠘\x1b[0m\x1b[33m⡄      ⢀⠇  ⠈\x1b[0m││25128     1.2.42.290 --no-san… 0.1%      0.5%      0B/s     │
│     │\x1b[33m⠊  ⠣⡀                                 ⡸⠃  ⠈⢱      ⡜    \x1b[0m││240045    steam                0.1%      0.3%      0B/s     │
│     │\x1b[33m    ⠱⡀⠤⠤⠤⠤⢄⣀                        ⣀⢠⠃     ⢣    ⢠⠃    \x1b[0m││240637    steamwebhelper       0.2%      0.3%      0B/s     │
│  0Mb│\x1b[33m     ⠑⠒⠒⠒⠒⠒⠒⠤⠤⠤⠤⠤⠤⠤⢄⣀⣀⣀⣀⣀⣀⡠⠤⠔⠒⠒⠢⠤⠤⠤⠔⠒⠃      ⠈⠦⠤⢄⣀⡜     \x1b[0m││25228     zellij               0.0%      0.2%      0B/s     │
│     └───────────────────────────────────────────────────────││3864      brave                0.0%      0.8%      0B/s     │
│   60s                                                     0s││1473      X                    0.2%      0.3%      0B/s     │
└─────────────────────────────────────────────────────────────┘└────────────────────────────────────────────────────────────┘
    """

    monaLines3 = f"""
┌ CPU ─ 1.04 0.71 0.50 ────────────────────────────────────────────────────────────────────────────────────┐┌───────────────┐
│100%│\x1b[31m            ⢠⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠒⠤⣀               \x1b[0m││\x1b[36mCPU     Use    \x1b[0m│
│    │\x1b[31m           ⢠⠃                                                                         ⠑⠢⢄⡀           \x1b[0m││               │
│    │\x1b[31m          ⢀⠎                                                                             ⠘⡄          \x1b[0m││All            │
│    │\x1b[31m         ⢀⠎                                                                               ⠘⡄         \x1b[0m││AVG     3%     │
│    │\x1b[31m         ⡜                                                                                 ⠘⡄        \x1b[0m││\x1b[31mCPU0    24%    \x1b[0m│
│    │\x1b[31m        ⡜                                                                                   ⠱⡀       \x1b[0m││\x1b[32mCPU1    8%     \x1b[0m│
│    │\x1b[31m       ⡰⠁                                                                                    ⠱⡀ ⢀ ⢀  \x1b[0m││\x1b[33mCPU2    32%    \x1b[0m│
│    │\x1b[31m      ⡰⠁\x1b[0m                                                                                \x1b[32m      ⢣⢠⠃⢣⡜  \x1b[0m││\x1b[34mCPU3    5%     \x1b[0m│
│    │\x1b[31m       ⡰⠁ \x1b[0m                                                                                \x1b[32m    ⡰⠁⠞⡰⢣⠁⠞\x1b[0m││\x1b[35mCPU4    9%     \x1b[0m│
│    │\x1b[31m   ⡔⠁  \x1b[0m                                                                                \x1b[34m      ⡔⠁⠋⢣⠃⢣⠋⢣\x1b[0m││\x1b[36mCPU5    10%    \x1b[0m│
│    │\x1b[31m  ⢀⠜    \x1b[0m                                                                                \x1b[36m   ⢀⠎⢀⡠⠔⠊⠒⢄⠔⠊\x1b[0m││\x1b[37mCPU6    13%    \x1b[0m│
│    │\x1b[31m⠤⢠⠊\x1b[0m\x1b[34m⣀⣀⣀⣀                                                                                   ⣀⠤⠒⠁⢀⡠⠔⠢⢄  \x1b[0m││\x1b[31mCPU7    19%    \x1b[0m│
│    │\x1b[31m⡠⠃ \x1b[0m\x1b[34m⣀   ⠉⣀⣀⣀⡠⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠔⠒⠒⠒⠉⠉⠃⠉⠔⠊⠁  ⠔⠒⠒⠒\x1b[0m││\x1b[32mCPU8    2%     \x1b[0m│
│  0%│\x1b[37m⠒⠒⠒⠉⠉⠉⠉⠉⠒⠒⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠉⠉⠉⠉⠉⠉⠉⠒⠒⠒⠒⠒⠒⠒⠤⠤⠤⠤⠤⠤⠔⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠉⠉⠁⠉⠉⠉⠁          \x1b[0m││\x1b[33mCPU9    24%    \x1b[0m│
│    └─────────────────────────────────────────────────────────────────────────────────────────────────────││\x1b[34mCPU10   4%     \x1b[0m│
│  60s                                                                                                   0s││\x1b[35mCPU11   15%    \x1b[0m│
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘└───────────────┘
┌ Memory ──────────────────────────────────────────────────────────────┐┌ Github Languages ─────────────────────────────────┐
│100%│                                     ┌──────────────────────────┐││\x1b[36m    Language▲                  usage%(t)           \x1b[0m│                                                       t)    \x1b[0m│
│    │                                     │RAM: 17%   10.9GiB/62.7GiB│││                                                   │
│    │                                     │SWP:  0%   0.0GiB/8.8GiB  │││    {stats.languages_sorted[0][0]}   {stats.languages_sorted[0][1]} %            │
│    │                                     └──────────────────────────┘││    {stats.languages_sorted[1][0]}   {stats.languages_sorted[1][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[2][0]}   {stats.languages_sorted[2][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[3][0]}   {stats.languages_sorted[3][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[4][0]}   {stats.languages_sorted[4][1]} %            │
│    │                                                                 ││    {stats.languages_sorted[5][0]}   {stats.languages_sorted[5][1]} %            │
│    │                                                                 ││                                                   │
│    │                                                                 │└───────────────────────────────────────────────────┘
│    │                                                                 │┌ Stats ────────────────────────────────────────────┐
│    │                                                                 ││\x1b[36m User          Commits    PRs   Rank   Percentile  \x1b[0m│
│    │                                                                 ││                                                   │
│    │                                                                 ││ {stats.account_name}{stats.total_commits_all_time}{stats.total_pull_requests_made}{stats.user_rank.level}{stats.user_rank.percentile}  │
│    │\x1b[33m⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒\x1b[0m││                                                   │
│  0%│\x1b[34m⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀\x1b[0m││                                                   │
│    └─────────────────────────────────────────────────────────────────││                                                   │
│  60s                                                               0s││                                                   │
└──────────────────────────────────────────────────────────────────────┘└───────────────────────────────────────────────────┘
┌ Network ────────────────────────────────────────────────────┐┌ Processes ─────────────────────────────────────────────────┐
│  1.2│                         ┌────────────────────────────┐││\x1b[36mPID(p)    Name(n)              CPU%(c)▼  Mem%(m)   R/s      \x1b[0m│
│     │                         │RX: 536.5Kb/s   All: 4.2GB  │││                                                            │
│     │                         │TX: 18.3Kb/s    All: 170.9MB│││230964    nvim                 0.0%      0.1%      0B/s     │
│     │                         └────────────────────────────┘││3899      brave                0.4%      0.5%      0B/s     │
│     │                                                       ││25228     zellij               0.0%      0.2%      0B/s     │
│  0.8│                                                       ││4235      brave                1.1%      0.8%      0B/s     │
│     │                                                       ││197176    .kitty-wrapped       0.2%      1.3%      0B/s     │
│     │                                                       ││2161      pipewire-pulse       0.1%      0.0%      0B/s     │
│     │ \x1b[33m                             ⢀                        \x1b[0m││240761    steamwebhelper       0.3%      0.4%      0B/s     │
│  0.4│\x1b[33m ⢀⢆           ⢠⢣              ⡎⢆           ⡜⡄          \x1b[0m││25190     .kitty-wrapped       0.1%      0.2%      0B/s     │
│     │\x1b[33m ⡜⠈⡆         ⢀⠇⠈⡆            ⡸⠃⠈⢆         ⡜⠁⢱          \x1b[0m││25128     1.2.42.290 --no-san… 0.1%      0.5%      0B/s     │
│     │\x1b[33m⢰⠁ ⠘⡄        ⡜\x1b[0m\x1b[35m⠎⠘⢸  \x1b[0m\x1b[33m        ⢰⠁  ⠈⢆   ⡀   ⡰⠁ ⠈⢇         \x1b[0m ││240045    steam                0.1%      0.3%      0B/s     │
│     │\x1b[33m⠇   ⠸⡀      ⡸\x1b[0m\x1b[35m⠊  ⠘⢇ \x1b[0m \x1b[33m       ⢀⠇    ⠈⠦⠤⠤⠤⣀⡀⡰⠁   ⠘⡄        \x1b[0m││240637    steamwebhelper       0.2%      0.3%      0B/s     │
│  0Mb│\x1b[33m     ⠱⠤⢄⣀⣀⡠⠴⠁    ⠘⣄⣀⠤⠤⠤⠤⠤⠔⠒⠉           ⠈⠁  \x1b[0m \x1b[35m  ⠱⠤⢄⣀⣀⡠⠤⠤⠤\x1b[0m││25004     .spotify-wrapped     0.1%      0.6%      16KB/s   │
│     └───────────────────────────────────────────────────────││3864      brave                0.0%      0.8%      0B/s     │
│   60s                                                     0s││1473      X                    0.2%      0.3%      0B/s     │
└─────────────────────────────────────────────────────────────┘└────────────────────────────────────────────────────────────┘
    """

    t.gen_text(monaLines0, 10, count=30)
    t.gen_text(monaLines1, 10, count=30)
    t.gen_text(monaLines2, 10, count=30)
    t.gen_text(monaLines3, 10, count=30)

    # t.toggle_show_cursor(True)

    t.gen_gif()

if __name__ == "__main__":
    main()
