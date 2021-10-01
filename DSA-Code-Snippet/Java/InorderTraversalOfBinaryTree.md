# Inorder Traversal of Binary Tree

## Explaination


> Uses of Inorder   In case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal  reversed can be used.  
>  Example: Inorder traversal for the above-given figure is 4 2 5 1 3.
> ### Algorithm for Inorder traversal
   >1. Traverse the left subtree, i.e., call Inorder(left-subtree)
   >2. Visit the root.
   >3. Traverse the right subtree, i.e., call Inorder(right-subtree)

## Code

```java  
class Node {
	int key;
	Node left, right;
	public Node(int item){
		key = item;
		left = right = null;
	}
}
  
class BinaryTree {
	// Root of Binary Tree
	Node root;
	BinaryTree() { root = null; }
  
	/* Print the nodes of given binary tree in inorder*/
	void printInorder(Node node){
		if (node == null){
		  return;
		}
		/* first recur on left child */
		printInorder(node.left);
		/* then print the data of node */
		System.out.print(node.key + " ");
		/* now recur on right child */
		printInorder(node.right);
	}
	// Wrappers over above recursive functions
	void printInorder(){
		printInorder(root);
	}
	// Main method
	public static void main(String[] args){
		BinaryTree tree = new BinaryTree();
	    tree.root = new Node(1);
	    tree.root.left = new Node(2);
	    tree.root.right = new Node(3);
	    tree.root.left.left = new Node(4);
	    tree.root.left.right = new Node(5);
	    //Printing tree
	    System.out.println("Inorder traversal of binary tree is: ");
	    tree.printInorder(); 
   }
}
```

## Output

```console
Inorder traversal of binary tree is: 
4 2 5 1 3 
```

## Contributed By
| Name | GitHub username | Institute |
|--|--|--|
| Abhinav Rajput | [AbhinavRajputEXE](https://github.com/AbhinavRajputEXE) | SRM, NCR campus, Modinagar |


