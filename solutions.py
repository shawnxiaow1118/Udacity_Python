
# Author: xwang

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
	# expand the string to unify odd and even situations
	expanded_str = "$#"
	for char in a:
		expanded_str += char + '#'
	expanded_str += "&"
	n = len(expanded_str)
	# list to record the dp values
	p = [0]*n
	# right most index of current longest palindrome
	mx = 0
	# center of current palindrome
	idx = 0
	# record the result len and center of final palindrom
	resLen = 0
	resCenter = 0
	for i in range(1,n-1):
		if mx > i:
			# min of symmetric points about the current palindrome's index
			p[i] = min(p[2*idx-i], mx-i)
		else:
			p[i] = 1
		while (expanded_str[i+p[i]] == expanded_str[i-p[i]]):
			# expand the current palindrom
			p[i]+=1
		if (mx < i+p[i]):
			# update 
			mx = i+p[i]
			idx = i
		if (resLen < p[i]):
			# update result information
			resLen = p[i]
			resCenter = i
	return a[(resCenter-resLen)/2:(resCenter+resLen)/2-1]

"""Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph 
	with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured.
"""
def find(i, parent):
	""" help function to find the root ancestor of a node
	"""
	while(parent[i]!=i):
		i = parent[i]
	return i

def union(x,y,parent,rank):
	""" help function to union two nodes with rank compression
	"""
	x_parent = parent[x]
	y_parent = parent[y]
	if (rank[x_parent] < rank[y_parent]):
		parent[x_parent] = y_parent
	elif (rank[x_parent] > rank[y_parent]):
		parent[y_parent] = x_parent
	else:
		parent[y_parent] = x_parent
		rank[x_parent] += 1

def question3(G):
	n = len(G)
	if n <= 2:
		return G
	edges = set()
	node_to_idx = {}
	count = 0
	# extract edges from the inputs
	for key in G.keys():
		# map index,easier for later find and union operation
		node_to_idx[key] = count
		count+=1
		for item in G[key]:
			# edge created based on order, this is undirected graph
			if key < item[0]:
				edge = (key, item[0], item[1])
			else:
				edge = (item[0], key, item[1])
			edges.add(edge)
	# sort edge based on the weight
	edges = sorted(edges, key=lambda item:item[2])
	parent = []
	rank = []
	res = []
	for i in range(n):
		parent.append(i)
		rank.append(0)
	for edge in edges:
		if find(node_to_idx[edge[0]], parent)!=find(node_to_idx[edge[1]], parent):
			res.append(edge)
			union(node_to_idx[edge[0]], node_to_idx[edge[1]], parent, rank)
	# construct desired results
	result = {}
	for item in res:
		A = item[0]
		B = item[1]
		weight = item[2]
		if A in result.keys():
			result[A].append((B,weight))
		else:
			result[A] = [(B,weight)]
		if B in result.keys():
			result[B].append((A,weight))
		else:
			result[B] = [(A,weight)]
	return result

"""Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root 
	that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents 
	of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and 
	the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree 
	represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a 
	non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order.
"""
def question4(T, r, n1, n2):
	# recursive method
	if len(T) <= 0:
		return 
	if (r == None):
		return
	if (n1 < r and n2 < r):
		return question4(T, T[r].index(1), n1, n2)
	elif (n1 > r and n2 > r):
		return question4(T, T[r][r:-1].index(1), n1, n2)
	return r


""" Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element 
	from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.
"""
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

def question5(ll, m):
	# run two pointer
	if m < 0 or ll == None:
		return
	first = ll
	second = ll
	if (ll is not None):
		for i in range(m):
			if (first == None):
				return
			else:
				first = first.next
	while(first != None):
		first = first.next
		second = second.next
	return second.data



######### Question1 test cases ###########
print("Question1")
print ("test case1: {}").format(question1("udacity", "au"))
# False
print ("test case2: {}").format(question1("udacity", "iacd"))
# True
print ("test case3: {}").format(question1("udacity", ""))
# False


######### Question2 test cases ###########
print("Question2")
print ("test case1: {}").format(question2("tgsdadse"))
# sdads
print ("test case2: {}").format(question2("123"))
# 1
print ("test case3: {}").format(question2(""))
# 


######### Question3 test cases ###########
print("Question3")
graph1 = {'A': [('B', 2), ('C', 2)],'B': [('A', 2), ('C', 5)], 'C': [('B', 5),  ('A', 2)]}
print ("test case1: {}").format(question3(graph1))
#  {'A': [('B', 2), ('C', 2)],'B': [('A', 2)], 'C': [('A', 2)]}
graph2 = {'A': [('B', 2), ('C', 8)],'B': [('A', 2), ('C', 5)], 'C': [('B', 5),  ('A', 8)]}
print ("test case2: {}").format(question3(graph2))
#  {'A': [('B', 2)],'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
graph3 = {}
print ("test case3: {}").format(question3(graph3))
# {}

######### Question4 test cases ###########
print("Question4")
# sdads
print ("test case1: {}").format(question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4))
# 3
print ("test case2: {}").format(question4([[0, 1, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          2))
# 1
print ("test case3: {}").format(question4([],3,1,2))
# None


######### Question5 test cases ###########
print("Question5")
head1 = Node(0)
head1.next = Node(10)
head1.next.next = Node(20)
head1.next.next.next = Node(50)
head1.next.next.next.next = Node(80)
print ("test case1: {}").format(question5(head1, 6))
# None
print ("test case2: {}").format(question5(head1, 2))
# 50
print ("test case3: {}").format(question5(None, 2))
# None