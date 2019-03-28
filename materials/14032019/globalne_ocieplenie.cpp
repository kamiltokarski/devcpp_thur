#include <bits/stdc++.h>

using namespace std;

int tab[1000009];
pair <int, int> srt[1000009];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    for(int i = 1; i <= n; i++)
    {
        cin >> tab[i];
        srt[i] = make_pair(tab[i], i);
    }
    sort(srt, srt+n+1);

    int lczwsp = 1;
    int pzmwd = 0;
    int i = 1;
    cout << 1 << " ";
    while(lczwsp != 0)
    {
        pzmwd++;
        while(srt[i].first <= pzmwd && i <= n)
        {
            int ilt = srt[i].second;
            while(i < n && tab[srt[i + 1].second] == tab[srt[i].second] && (srt[i].second + 1) == srt[i + 1].second) {
                // cout << srt[i].second + 1 << " = " << srt[i + 1].second << endl;
                ++i;
            }

            // cout << "te same wyspy od " << ilt << " do " << srt[i].second << endl;
            if(tab[ilt-1] > pzmwd
               && tab[srt[i].second+1] > pzmwd)
            {
                lczwsp++;
            }
            else if(tab[ilt-1] <= pzmwd
                    && tab[srt[i].second+1] <= pzmwd)
            {
                lczwsp--;
            }
            i++;
        }
        cout << lczwsp << " ";
    }
    return 0;
}