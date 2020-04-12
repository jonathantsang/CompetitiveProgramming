class Solution:
    def entityParser(self, text: str) -> str:
        ans = []
        i = 0
        while i < len(text):
            if text[i] == "&":
                if i+6 <= len(text) and text[i:i+6] == "&quot;":
                    ans.append('"')
                    i += 6
                elif i+6 <= len(text) and text[i:i+6] == "&apos;":
                    ans.append("'")
                    i += 6
                elif i+5 <= len(text) and text[i:i+5] == "&amp;":
                    ans.append("&")
                    i += 5
                elif i+4 <= len(text) and text[i:i+4] == "&gt;":
                    ans.append(">")
                    i += 4
                elif i+4 <= len(text) and text[i:i+4] == "&lt;":
                    ans.append("<")
                    i += 4
                elif i+7 <= len(text) and text[i:i+7] == "&frasl;":
                    ans.append("/")
                    i += 7
                else:
                    ans.append(text[i])
                    i += 1
            else:
                ans.append(text[i])
                i += 1
        return "".join(ans)
                
