class Solution(object):
    def postorder(self, root):

        if root is None:
            return []

        result = []

        for child in root.children:
            result += self.postorder(child)

        result.append(root.val)

        return result