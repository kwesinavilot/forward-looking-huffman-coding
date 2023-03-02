import heapq
import sys
import time

class ForwardHuffmanEncoder:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.encoded_data = ""

    def make_frequency_dict(self, data):
        """
        Create a dictionary with the frequency of each symbol in the input data
        """
        # check if the input data is a string
        if not isinstance(data, str):
            raise ValueError("Invalid input data. Data must be a string.")
        # create an empty frequency dictionary
        frequency = {}
        # count the frequency of each symbol
        for symbol in data:
            if symbol not in frequency:
                frequency[symbol] = 0
            frequency[symbol] += 1
        return frequency

    def make_heap(self, frequency):
        """
        Create a heap from the frequency dictionary
        """
        # add each symbol to the heap
        for key in frequency:
            heapq.heappush(self.heap, (frequency[key], key))

    def merge_nodes(self):
        """
        Merge nodes of the heap until there's only one left
        """
        # merge nodes until there's only one left
        while len(self.heap) > 1:
            lo = heapq.heappop(self.heap)
            hi = heapq.heappop(self.heap)

            # merge the two nodes and add it back to the heap
            merged = (lo[0] + hi[0], lo[1] + hi[1])
            heapq.heappush(self.heap, merged)

            # update the codes for each symbol in the merged nodes
            for symbol in lo[1]:
                self.codes[symbol] = '0' + self.codes.get(symbol, '')
            for symbol in hi[1]:
                self.codes[symbol] = '1' + self.codes.get(symbol, '')

    def encode_data(self, data):
        """
        Encode the input data with the created codes
        """
        # add the encoded data for each symbol
        for symbol in data:
            self.encoded_data += self.codes[symbol]
    
    def update_tree(self, symbol):
        """
        Update the tree and encoded data when a new symbol is added
        """
        #increment the frequency of the symbol in the heap
        for node in self.heap:
            if symbol in node[1:]:
                node[0] += 1
            break

            # rebuild the heap
            heapq.heapify(self.heap)
            
            # update the tree
            self.merge_nodes()
            self.make_codes()

            # update the encoded data
            self.encoded_data = ""
            self.encode_data(symbol)

    def compress(self):
        """
        Compress the input data entered by the user
        """
        data = input("\nEnter the data to compress: ")
        frequency = self.make_frequency_dict(data)
        self.make_heap(frequency)
        self.merge_nodes()
        self.encode_data(data)

        print("\nCompressed data: ", self.encoded_data)

    def decode_data(self, encoded_data):
        """
        Decode the encoded data back to the original data
        """
        data = ""
        current_code = ""

        for bit in encoded_data:
            current_code += bit
            for symbol, code in self.codes.items():
                if current_code == code:
                    data += symbol
                    current_code = ""
                    break

        return data

    def decompress(self):
        """
        Decompress the encoded data entered by the user
        """
        encoded_data = input("\nEnter the encoded data to decompress: ")
        data = self.decode_data(encoded_data)

        print("\nDecompressed data: ", data)

# Create an instance of the ForwardHuffmanEncoder class
encoder = ForwardHuffmanEncoder()

# Compress and decompress user input

while True:
    user_input = input("Welcome to the Novel Forward-looking Huffman Coding\n"
      "Enter:\n"
      "'c' to compress data\n"
      "'d' to decompress data\n"
    #   "'u' to update the tree\n"
      "'q' to quit\n"
      "Response: ")
    
    if user_input.lower() == 'c':
        start_time = time.time()
        encoder.compress()
        end_time = time.time()
        print("\nTime taken: {:.6f} seconds".format(end_time - start_time))
        print()
    elif user_input.lower() == 'd':
        start_time = time.time()
        encoder.decompress()
        end_time = time.time()
        print("\nTime taken: {:.6f} seconds".format(end_time - start_time))
        print()
    # elif user_input.lower() == 'u':
    #     update()
    elif user_input.lower() == 'q':
        sys.exit()
    else:
        print("Invalid input. Please try again.")
