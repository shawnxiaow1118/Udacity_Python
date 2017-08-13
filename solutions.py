""" Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad",
	then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.
"""
def question1(s, t):
	counter = {}
	# construct dict for string t's characters
	for char in t:
		if char in counter.keys():
			counter[char]+=1
		else:
			counter[char]=1
	# start from the index 0 and to see whether we can find substrig that is anagram of t
	# which is determined by a dictionary
	idx = 0
	for i in range(len(s)):
		if s[i] in counter.keys():
			# s[i] in dict's key set
			if counter[s[i]] == 0:
				# character appear too many
				j = idx
				# move the cursor right to solve the redundant characters problem
				while(s[j]!=s[i]):
					counter[s[j]]+=1
					j+=1
				idx = j
			else:
				# decrease the counter acccordingly
				counter[s[i]]-=1
				if (sum(counter.values())==0):
					return True
		else:
			# s[i] not is not contained in t, then start the same process from i+1
			for j in range(idx, i):
				counter[s[j]]+=1
			idx = i+1
	return False


""" Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), 
	and return a string.
"""
def question2(a):
	# Manacher's Algorithms, based on the assumption that the string is normal one, doesn't contain & I used in the algorithm
	expanded_str = "$#"
	for char in a:
		expanded_str += char + '#'
	expanded_str += "&"
	n = len(expanded_str)
	p = [0]*n
	mx = 0
	idx = 0
	resLen = 0
	resCenter = 0
	for i in range(1,n-1):
		if mx > i:
			p[i] = min(p[2*idx-i], mx-i)
		else:
			p[i] = 1
		while (expanded_str[i+p[i]] == expanded_str[i-p[i]]):
			p[i]+=1
		if (mx < i+p[i]):
			mx = i+p[i]
			idx = i
		if (resLen < p[i]):
			resLen = p[i]
			resCenter = i
	return a[(resCenter-resLen)/2:(resCenter+resLen)/2-1]

"""Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph 
	with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured.
"""
def question3(G):
	return

"""Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root 
	that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents 
	of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and 
	the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree 
	represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a 
	non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order.
"""
def question4(T, r, n1, n2):
	return


""" Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element 
	from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.
"""
def question5(ll, m):
	return



######### Question1 test cases ###########
print("Question1")
# print question1("udacity", "au")
# False
# print question1("udacity", "iacd")
# True
# print question1("udacity", "")
# False


######### Question2 test cases ###########
print("Question2")
print question2("tgsdadse")
# sdads
print question2("123")
# 1
print question2("")
# 
