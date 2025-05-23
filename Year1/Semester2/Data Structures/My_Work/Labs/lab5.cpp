#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

struct TrieNode
{
    unordered_map<char, TrieNode *> children;
    bool EOW;
    TrieNode() : EOW(false) {}
};

class Trie
{
    TrieNode *root;

    void getAllWords(TrieNode *curr, string prefix, vector<string> &words)
    {
        if (curr->EOW)
            words.push_back(prefix);
        for (auto &[ch, child] : curr->children)
            if (child)
                getAllWords(child, prefix + ch, words);
    }

    int levDist(string a, string b)
    {
        int n = a.size();
        int m = b.size();
        vector<vector<int>> mat(n + 1, vector<int>(m + 1));
        for (int i = 0; i <= n; i++)
            mat[i][0] = i;
        for (int j = 0; j <= m; j++)
            mat[0][j] = j;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= m; j++)
            {
                if (a[i - 1] == b[j - 1])
                    mat[i][j] = mat[i - 1][j - 1];
                else
                    mat[i][j] = 1 + min(mat[i][j - 1], min(mat[i - 1][j - 1], mat[i - 1][j]));
            }
        }
        return mat[n][m];
    }

public:
    Trie()
    {
        root = new TrieNode();
    }

    void insert(string word)
    {
        TrieNode *curr = root;
        for (auto ch : word)
        {
            if (!curr->children[ch])
                curr->children[ch] = new TrieNode();
            curr = curr->children[ch];
        }
        curr->EOW = true;
    }

    bool search(string word)
    {
        TrieNode *curr = root;
        for (auto ch : word)
        {
            if (!curr->children[ch])
                return false;
            curr = curr->children[ch];
        }
        return curr->EOW;
    }

    vector<string> autoComplete(string prefix)
    {
        vector<string> res;
        TrieNode *curr = root;
        for (auto ch : prefix)
        {
            if (!curr->children[ch])
                return res;
            curr = curr->children[ch];
        }
        getAllWords(curr, prefix, res);
        return res;
    }

    vector<string> autoCorrect(string Iword, int maxDist = 1)
    {
        vector<string> words;
        vector<string> res;
        getAllWords(root, "", words);
        for (auto word : words)
        {
            if (levDist(Iword, word) <= maxDist)
                res.push_back(word);
        }
        return res;
    }
};

int main()
{
    Trie trie;

    // Insert words
    vector<string> dictionary;
    dictionary.push_back("flower");
    dictionary.push_back("flow");
    dictionary.push_back("flight");
    dictionary.push_back("flown");
    dictionary.push_back("flop");
    dictionary.push_back("flute");
    dictionary.push_back("dog");
    dictionary.push_back("deer");
    dictionary.push_back("deal");
    dictionary.push_back("cat");
    dictionary.push_back("car");
    dictionary.push_back("cart");

    for (const string &word : dictionary)
    {
        trie.insert(word);
    }

    // Test search
    cout << "Search for 'flow': " << (trie.search("flow") ? "Found" : "Not Found") << endl;
    cout << "Search for 'flown': " << (trie.search("flown") ? "Found" : "Not Found") << endl;
    cout << "Search for 'flaw': " << (trie.search("flaw") ? "Found" : "Not Found") << endl;

    // Test autocomplete
    cout << "\nAutocomplete for 'fl': ";
    vector<string> ac = trie.autoComplete("fl");
    for (const string &word : ac)
        cout << word << " ";
    cout << endl;

    // Test autocorrect
    cout << "\nAutocorrect for 'fliht' (maxDist = 2): ";
    vector<string> corrected = trie.autoCorrect("fliht", 2);
    for (const string &word : corrected)
        cout << word << " ";
    cout << endl;

    return 0;
}