class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prerequest_for = defaultdict(set)

        # каждому номеру курса соответствует сет из номеров курсов, которые нужны чтобы пройти данный
        for course, pre in prerequisites:
            prerequest_for[course].add(pre)

        # проверяем, можно ли пройти course
        def dive(course, to_be_taken, bad_courses):
            if not prerequest_for[course]:  # если у курса нет предварительных курсов, то ок, можно пройти
                return True

            if course in bad_courses:
                return False

            if course in to_be_taken:  # если данный курс входит в список того, что надо пройти, чтобы пройти данный курс (то есть есть циклическая зависимость), то это плохой курс, его не возможно пройти. добавим его в список плохих крусов, чтобы больше не смотреть в его зависимости, а сразу говорить, что он плохой
                bad_courses.add(course)
                return False

            to_be_taken.add(
                course)  # добавляем курс в список того, что надо пройти перед тем как рассматривать его зависимости. так мы поймаем цикл предыдущим ифом

            for c in prerequest_for[course]:
                if not dive(c, to_be_taken, bad_courses):
                    bad_courses.add(c)
                    return False

            prerequest_for[
                course] = []  # это хороший курс, больше не будем дайвить в его зависимости, потому что мы уж знаем, что с ними всё ок

            return True

        bad_courses = set()

        for c in range(numCourses):
            if not dive(c, set(), bad_courses):
                return False

        return True
