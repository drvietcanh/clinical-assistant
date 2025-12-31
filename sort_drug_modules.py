import os
import ast
import re

DRUG_MODULES_DIR = r"d:\1 medical\drugs\drug_modules"

def get_file_content(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def sort_dictionary_in_text(text, filepath):
    """
    Parses the text, finds top-level uppercase dictionaries,
    and sorts their keys textually to preserve comments/structure.
    """
    try:
        tree = ast.parse(text)
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return text

    # Find assignments to dictionaries
    replacements = []

    for node in tree.body:
        if isinstance(node, ast.Assign):
            # Check if it's an assignment to a NAME (not attribute/subscript)
            target = node.targets[0]
            if isinstance(target, ast.Name):
                var_name = target.id
                # Heuristic: Only target uppercase variables like HEMATOLOGY_DRUGS, AMINOGLYCOSIDE_ANTIBIOTICS
                # Or variables ending in _DRUGS or _ANTIBIOTICS
                if (var_name.isupper() and isinstance(node.value, ast.Dict)):
                    print(f"Found dictionary to sort: {var_name} in {os.path.basename(filepath)}")
                    
                    dict_node = node.value
                    if not dict_node.keys:
                        continue
                    
                    # We need to extract the text blocks for each key
                    lines = text.splitlines(keepends=True)
                    
                    items = []
                    keys = dict_node.keys
                    values = dict_node.values
                    
                    # Sort logic
                    # We need to capture the text span for each item.
                    # Span starts at the key's lineno. 
                    # Ends at the start of the NEXT key, or the end of the dict.
                    
                    # Let's collect spans
                    spans = []
                    for i, (k, v) in enumerate(zip(keys, values)):
                        if not isinstance(k, (ast.Str, ast.Constant)):
                            print(f"Skipping {var_name}, non-string key found.")
                            return text # Abort for this file if complex keys
                        
                        # Get key string for sorting
                        key_val = k.s if hasattr(k, 's') else k.value
                        
                        start_line = k.lineno - 1 # 0-indexed
                        
                        # End line is tricky. It's the end of value. 
                        # But we also want to include any trailing comma and comments up to the next key.
                        # Simplification: End line is the start line of the NEXT key - 1? 
                        # Or we can just scan until we hit the next valid key start?
                        
                        if i < len(keys) - 1:
                            next_k = keys[i+1]
                            end_line = next_k.lineno - 1
                        else:
                            # Last item. Go until the closing brace of the dict.
                            # We can use the dict_node.end_lineno? 
                            # Only available in Python 3.8+. Assuming 3.8+
                            end_line = getattr(dict_node, 'end_lineno', -1) 
                            if end_line == -1:
                                # Fallback scanning
                                end_line = len(lines) 
                            else:
                                end_line = end_line - 1 # Exclude the closing brace line usually?
                                # Actually the closing brace might be on a new line or same line.
                                # Let's be careful.
                                pass
                        
                        spans.append({
                            'key': key_val,
                            'start_line': start_line,
                            'end_line': end_line, # Exclusive (for slicing logic later)
                            'value_node': v
                        })
                    
                    # Refine end_lines
                    # For item [i], the text chunk is lines[start_line : end_line]
                    # But we need to be careful about the *actual* split point.
                    # A better way: 
                    # Chunk [i] goes from `key[i].lineno` until `key[i+1].lineno`.
                    # But if there are comments *before* key[i+1], they might belong to key[i+1].
                    # Python AST doesn't link comments.
                    
                    # Alternative Strategy:
                    # Just sort the AST nodes and rebuild? No, formatting loss.
                    
                    # "Chunk" Strategy refinement:
                    # Use the raw text. 
                    # Assume standard formatting: 
                    #    "Key": {
                    #        ...
                    #    },
                    #    "Next": ...
                    
                    # Find the exact byte offsets?
                    # Python source code is easier to handle by lines usually.
                    
                    # Let's try to grab lines.
                    # If I take everything from `k.lineno` up to `next_k.lineno`, 
                    # then comments between items will allow to the *previous* item.
                    # Usually:
                    # },
                    # # Comment for next item
                    # "NextItem": ...
                    
                    # If I attach comments to the *previous* item, they will move with the previous item.
                    # This is BAD if the comment is a header for the next item.
                    # This is GOOD if the comment is a footer or trailing comment.
                    
                    # In this codebase, comments seem to be inside values or docstrings.
                    # Top-level comments between keys are rare in the viewed files.
                    # Let's check `hematology/__init__.py` again.
                    # It's dense.
                    
                    # Let's stick to: Chunk = Start of Key -> Start of Next Key.
                    # This means trailing commas and newlines belong to the item.
                    # The last item needs special handling to NOT include the closing brace '}'.
                    
                    # We need to find the specific line with '}' that closes the dict.
                    # AST tells us dict_node.end_lineno.
                    
                    # Let's build the chunks.
                    chunks = []
                    full_keys = []
                    
                    for i in range(len(keys)):
                        k_start = keys[i].lineno - 1
                        
                        if i < len(keys) - 1:
                            k_end = keys[i+1].lineno - 1
                        else:
                            # Last item
                            # Find the line with the closing brace '}'
                            # It is likely strict formatting: the last line of the dict is '}' or '};'
                            # or '    }'
                            # Let's traverse backwards from dict end or start from last value end.
                            
                            last_val = values[i]
                            # Start looking for '}' after the last value ends
                            search_start = getattr(last_val, 'end_lineno', last_val.lineno) - 1
                            
                            # Scan forward from search_start until we find a line containing `}` at the appropriate indentation?
                            # Or just use the AST end_lineno if available.
                            ast_end = getattr(dict_node, 'end_lineno', -1)
                            if ast_end != -1:
                                # The dict ends at ast_end. 
                                # The content of the last value is up to ast_end-1 usually?
                                # If the dict is:
                                # {
                                #   "A": 1
                                # }  <-- ast_end is here.
                                k_end = ast_end - 1
                            else:
                                # Fallback difficult without AST end info (py3.7-)
                                # Assuming py3.8+ for tool.
                                raise RuntimeError("Python version too old, lacking end_lineno")
                        
                        # Grab lines
                        fragment = lines[k_start:k_end]
                        chunks.append("".join(fragment))
                        full_keys.append(items[i] if i < len(items) else spans[i]['key'])

                    # Now sort chunks by key
                    # zip keys and chunks
                    paired = list(zip(full_keys, chunks))
                    paired.sort(key=lambda x: x[0])
                    
                    sorted_chunks = [p[1] for p in paired]
                    
                    # Fix comma logic?
                    # If we blindly reorder, the last item might not have a comma, 
                    # and the former last item (now in middle) might not have a comma.
                    # And the item moved to last position WILL have a comma.
                    # We need to standardize commas.
                    # Ensure EVERY chunk has a trailing comma, except possibly the last one (but Python allows trailing comma).
                    # Best practice: Add trailing comma to ALL chunks.
                    
                    final_chunks = []
                    for chunk in sorted_chunks:
                        # strip trailing whitespace/newlines to check last char
                        rstrip_chunk = chunk.rstrip()
                        if rstrip_chunk.endswith(','):
                             final_chunks.append(chunk)
                        else:
                            # Add comma
                            # Where? before the last newline.
                            # Chunk usually ends with newline.
                            if chunk.endswith('\n'):
                                final_chunks.append(chunk.rstrip('\n') + ',\n')
                            else:
                                final_chunks.append(chunk + ',')
                                
                    # Join them
                    new_body = "".join(final_chunks)
                    
                    # Replace in original text
                    # Range is keys[0].lineno-1 to (last_item_end_line)
                    # The start is clean.
                    # The end of the replacement zone is the end-line of the last item in the ORIGINAL order.
                    
                    # Original range:
                    # Start: keys[0].lineno - 1
                    # End: (keys[-1] end logic calculated above)
                    
                    orig_start_idx = keys[0].lineno - 1
                    
                    # Calculate original end index similarly to loop
                    ast_end = getattr(dict_node, 'end_lineno', -1)
                    orig_end_idx = ast_end - 1
                         
                    # Wait, if the closing brace is on a separate line (usual), we replace up to that line.
                    # What if closing brace is `}`, and we replace everything before it?
                    # Yes.
                    
                    # Special check: Does the last item include the closing brace?
                    # My logic for `k_end` for the last item was `ast_end - 1`.
                    # This implies valid range is `lines[orig_start_idx : ast_end - 1]`.
                    # Let's verify if `lines[ast_end-1]` is the closing brace line.
                    # Yes, usually.
                    
                    # Replacements need to be done carefully (offsets change if we do multiple, but here we do one big block per dict)
                    # Actually, if we modify the list of lines in place, indexes shift.
                    # But we can just use the line list.
                    
                    # Apply replacement to `lines`
                    # We can't do this easily if we process multiple dicts.
                    # But usually one file = one main dict.
                    # Let's assume we do them sequentially or just one.
                    
                    replacements.append((orig_start_idx, orig_end_idx, new_body))

    # Apply replacements in reverse order to preserve line numbers
    lines = text.splitlines(keepends=True)
    replacements.sort(key=lambda x: x[0], reverse=True)
    
    for start, end, content in replacements:
        # Replace slice
        # Note: end is exclusive index from our loop logic?
        # My logic: `k_end` was exclusive.
        # So `lines[start:end]` should be replaced.
        
        # Verify safety: Print header of repl
        # print(f"Replacing lines {start+1} to {end}")
        # print("Old Start:", lines[start][:20])
        # print("Old End:", lines[end-1][:20])
         
        lines[start:end] = [content]
        
    return "".join(lines)


def process_files():
    for root, dirs, files in os.walk(DRUG_MODULES_DIR):
        for file in files:
            if file.endswith(".py") and file != "__init__.py": 
                # Also include __init__.py actually? 
                # The user's target files ARE __init__.py files in subfolders.
                pass
                
        # Actually, iterate ALL .py files
        for file in files:
            if not file.endswith(".py"):
                continue
                
            filepath = os.path.join(root, file)
            print(f"Processing {filepath}...")
            
            content = get_file_content(filepath)
            new_content = sort_dictionary_in_text(content, filepath)
            
            if new_content != content:
                print(f"Writing changes to {filepath}")
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
            else:
                print("No changes needed.")

if __name__ == "__main__":
    process_files()
