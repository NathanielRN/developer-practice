from typing import List

boys_test = ['John', 'Mike', 'Jason']

girls_test = ['Alice', 'Miranda', 'Rhea']

# ['Mike', 'Jason']

# ['Alice', 'Rhea']


def all_pairs_of_students(boys_in, girls_in) -> List[List[str]]:
    if len(boys_in) == 1 and len(girls_in) == 1:
        return [[boys_in[0], girls_in[0]]]
    
    all_pairs = []
    boys = boys_in[:]
    girls = girls_in[:]

    for boy in boys_in:
        for girl in girls_in:
            boys.remove(boy)
            girls.remove(girl)
            all_pairs.extend(all_pairs_of_students(boys, girls))
            boys.append(boy)
            girls.append(girl)

    return set(all_pairs)

ans = all_pairs_of_students(boys_test, girls_test)

print(ans)