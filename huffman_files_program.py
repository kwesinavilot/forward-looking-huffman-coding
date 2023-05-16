# import sys
# import time
# from NovelForwardLookingHuffman import ForwardLookingHuffmanReal

# # initialize the tree class
# huffman = ForwardLookingHuffmanReal()

# while True:
#     user_input = input("Welcome to the Novel Forward-looking Huffman Coding\n"
#                        "Enter:\n"
#                        "'c' to compress data\n"
#                        "'d' to decompress data\n"
#                        "'q' to quit\n"
#                        "Response: ")

#     if user_input.lower() == 'c':
#         input_filename = input("Enter the filename to compress: ")
#         output_filename = input("Enter the filename to store the compressed data: ")
#         with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
#             data = input_file.read().encode()
#             # print(data)
#             start_time = time.time()
#             compressed_data = huffman.compress(data)
#             end_time = time.time()
#             output_file.write(compressed_data)
#             print("\nTime taken to compress the data: {:.6f} seconds".format(end_time - start_time))
#             print(f"Compressed data saved in {output_filename}\n")

#     elif user_input.lower() == 'd':
#         input_filename = input("Enter the filename to decompress: ")
#         output_filename = input("Enter the filename to store the decompressed data: ")
#         with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
#             data = input_file.read()
#             start_time = time.time()
#             decompressed_data = huffman.decompress(data)
#             end_time = time.time()
#             output_file.write(decompressed_data)
#             print("\nTime taken to decompress the data: {:.6f} seconds".format(end_time - start_time))
#             print(f"Decompressed data saved in {output_filename}\n")

#     elif user_input.lower() == 'q':
#         sys.exit()

#     else:
#         print("Invalid input. Please try again.")


import sys
import time
import os
from NovelForwardLookingHuffman import NovelForwardLookingHuffman

# initialize the tree class
huffman = NovelForwardLookingHuffman()

while True:
    user_input = input("Welcome to the Novel Forward-looking Huffman Coding\n"
                       "Enter:\n"
                       "'c' to compress data\n"
                       "'d' to decompress data\n"
                       "'q' to quit\n"
                       "Response: ")

    if user_input.lower() == 'c':
        input_filename = input("Enter the filename to compress: ")
        output_filename = input("Enter the filename to store the compressed data: ")
        with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
            print('Begininig sequence...\nReading file data...', flush=True)
            
            original_size = os.path.getsize(input_filename)

            data = input_file.read()

            print('File reading complete.\nRunning compression sequence...', flush=True)

            start_time = time.time()
            compressed_data = huffman.compress(data)
            end_time = time.time()

            print('Compression complete!\nWriting to new file...', flush=True)
            output_file.write(compressed_data)

            compressed_size = os.path.getsize(output_filename)
            compression_ratio = original_size / compressed_size

            print(f"Compressed data saved in {output_filename}")
            print('\nOriginal File Size: ', original_size)
            print('\nNew File Size: ', compressed_size)
            print("Time taken to compress the data: {:.6f} seconds".format(end_time - start_time))
            print(f"Compression Ratio: {compression_ratio:.3f}\n")

    elif user_input.lower() == 'd':
        input_filename = input("Enter the filename to decompress: ")
        output_filename = input("Enter the filename to store the decompressed data: ")
        with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
            data = input_file.read()
            start_time = time.time()
            decompressed_data = huffman.decompress(data)
            end_time = time.time()
            output_file.write(decompressed_data)
            original_size = os.path.getsize(input_filename)
            compressed_size = os.path.getsize(output_filename)
            compression_ratio = (original_size - compressed_size) / original_size
            print("\nTime taken to decompress the data: {:.6f} seconds".format(end_time - start_time))
            print(f"Decompressed data saved in {output_filename}")
            print(f"Compression Ratio: {compression_ratio:.3f}\n")

    elif user_input.lower() == 'q':
        sys.exit()

    else:
        print("Invalid input. Please try again.")
