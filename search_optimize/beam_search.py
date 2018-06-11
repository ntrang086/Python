import math

def beam_search(inputs, beam_width=3):
    """Implement a basic beam search algorithm that can be used as a decoder
    for text generation or machine translation."""
    # Top sequences and their corresponding scores
    seqs_scores = [[[], 0.0]]
    for values in inputs:
        # Get the indices of the top values
        top_idx = sorted(range(len(values)), key=lambda x:values[x], 
                            reverse=True)[:beam_width]
        top_log_probs = [math.log(values[idx]) for idx in top_idx]
        all_candidates = []
        # Predict the next item in each of the top sequences
        for seq, score in seqs_scores:
            for i in range(beam_width):
                next_seq = seq[:]
                next_seq.append(top_idx[i])
                next_score = score + top_log_probs[i]
                all_candidates.append([next_seq, next_score])
        # Update seqs_scores with the best beam_width candidates
        seqs_scores = sorted(all_candidates, 
                             key=lambda x:x[1], reverse=True)[:beam_width]
    return seqs_scores

if __name__ == "__main__":
    # Define a sequence of 3 words over a vocabulary of 5 words
    inputs = [[0.1, 0.2, 0.3, 0.4, 0.5],
              [0.5, 0.4, 0.3, 0.2, 0.1],
              [0.1, 0.2, 0.3, 0.4, 0.5]]
    result = beam_search(inputs, 3)
    for seq in result:
        print(seq)