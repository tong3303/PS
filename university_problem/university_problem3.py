'''이 코드와 내 코드의 차이점
- 트리를 관리하는 자료구조
- build_tree()
'''

import sys

class TreeProcessor:
    def __init__(self):
        self.nodes = []  # 노드 저장소: (type, name, left_idx, right_idx)
        self.count = 0
        self.tokens = []

    # "(", 단말 노드에 따라 노드 생성, left_idx, next_idx 리턴하는 재귀 구조
    def build_tree(self, idx):
        """괄호 구조를 해석하여 노드 리스트를 생성"""
        token = self.tokens[idx]
        
        if token == '(':
            # 1. 내부 노드 이름 부여 (Preorder 순서)
            current_name = f"r{self.count}"
            self.count += 1
            
            # 2. 왼쪽 자식 재귀 탐색
            left_idx, next_idx = self.build_tree(idx + 1)
            # 3. 오른쪽 자식 재귀 탐색
            right_idx, next_idx = self.build_tree(next_idx)
            
            # 4. 현재 노드 저장 (내부 노드는 양쪽 자식 인덱스를 가짐)
            self.nodes.append(('tree', current_name, left_idx, right_idx))
            return len(self.nodes) - 1, next_idx + 1 # ')' 건너뛰기
        else:
            # 단말 노드 처리
            self.nodes.append(('node', token, None, None))
            return len(self.nodes) - 1, idx + 1

    # 전위 순회
    def get_preorder(self, curr_idx, result):
        node_type, name, left, right = self.nodes[curr_idx]
        result.append(name)
        
        if node_type == 'tree':
            self.get_preorder(left, result)
            self.get_preorder(right, result)

    # 후위 순회
    def get_inorder(self, curr_idx, result):
        node_type, name, left, right = self.nodes[curr_idx]
        
        if node_type == 'tree':
            self.get_inorder(left, result)
            result.append(name)
            self.get_inorder(right, result)
        else:
            result.append(name)

# 메인 로직
def main():
    # 모든 입력을 한 번에 읽어 처리 (효율성)
    input = sys.stdin.readline
    total = int(input())
    
    for i in range(total):
        line = input().strip()
        if not line: continue
            
        # 프로세서 초기화
        processor = TreeProcessor()
        processor.tokens = line.split()
        
        # 트리 구축
        root_idx, _ = processor.build_tree(0)
        
        # 결과 수집
        pre_res, in_res = [], []
        processor.get_preorder(root_idx, pre_res)
        processor.get_inorder(root_idx, in_res)
        
        # 출력 형식에 맞춰 출력
        print("Preorder 결과:")
        print('\n'.join(pre_res))
        print("Inorder 결과:")
        print('\n'.join(in_res))

if __name__ == "__main__":
    main()

