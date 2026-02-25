class Solution:
    def findDuplicate(self, ps: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for p in ps:
            parts = p.split(" ")
            directory = parts[0]

            for file_info in parts[1:]:
                name, content = file_info.split("(")
                content = content[:-1]  
                
                full_p = directory + "/" + name
                map[content].append(full_p)
        return [files for files in map.values() if len(files) > 1]
