def solution(id_pw, db):
    answer = 'fail'
    for i in db:
        if i[0] == id_pw[0] and i[1] ==id_pw[1]:
            answer ="login"
            break
        elif i[0] == id_pw[0] and i[1] !=id_pw[1]:
            answer ="wrong pw"
            break
        
    return answer