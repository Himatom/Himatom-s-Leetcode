class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> result;
        if (s.empty() || words.empty()) return result;
        
        int wordLen = words[0].length();
        int numWords = words.size();
        int strLen = s.length();
        
        // Store the frequency of each word in the target array
        unordered_map<string, int> wordCount;
        for (const string& word : words) {
            wordCount[word]++;
        }
        
        // Run the sliding window for each possible offset
        for (int i = 0; i < wordLen; ++i) {
            int left = i;
            int right = i;
            int validWords = 0;
            unordered_map<string, int> currentCount;
            
            while (right + wordLen <= strLen) {
                // Extract the next word of length 'wordLen'
                string word = s.substr(right, wordLen);
                right += wordLen;
                
                // If it's a valid word from the list
                if (wordCount.count(word)) {
                    currentCount[word]++;
                    validWords++;
                    
                    // If we have more of 'word' than required, slide the left pointer
                    while (currentCount[word] > wordCount[word]) {
                        string leftWord = s.substr(left, wordLen);
                        currentCount[leftWord]--;
                        validWords--;
                        left += wordLen;
                    }
                    
                    // If we successfully matched all words, record the starting index
                    if (validWords == numWords) {
                        result.push_back(left);
                    }
                } 
                // If it's an invalid word, reset the current window
                else {
                    currentCount.clear();
                    validWords = 0;
                    left = right;
                }
            }
        }
        
        return result;
        
    }
};