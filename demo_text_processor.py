"""Demonstration of text_processor module functionality."""

from text_processor import (
    count_words,
    count_sentences,
    reverse_text,
    capitalize_words,
    remove_extra_spaces
)

def main():
    """Demonstrate all text processing functions."""
    
    sample_text = "  hello   world!  this is a demo. amazing stuff? yes it is  "
    
    print("=" * 60)
    print("Text Processor Demo")
    print("=" * 60)
    
    print(f"\nOriginal text: '{sample_text}'")
    print(f"Original text length: {len(sample_text)} characters")
    
    print("\n" + "-" * 60)
    print("Processing Results:")
    print("-" * 60)
    
    # Clean up extra spaces
    cleaned = remove_extra_spaces(sample_text)
    print(f"\n1. After removing extra spaces:")
    print(f"   '{cleaned}'")
    
    # Count words
    word_count = count_words(cleaned)
    print(f"\n2. Word count:")
    print(f"   {word_count} words")
    
    # Count sentences
    sentence_count = count_sentences(cleaned)
    print(f"\n3. Sentence count:")
    print(f"   {sentence_count} sentences")
    
    # Capitalize words
    capitalized = capitalize_words(cleaned)
    print(f"\n4. After capitalizing each word:")
    print(f"   '{capitalized}'")
    
    # Reverse text
    reversed_text = reverse_text(cleaned)
    print(f"\n5. Reversed text:")
    print(f"   '{reversed_text}'")
    
    print("\n" + "=" * 60)
    print("Demo complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
