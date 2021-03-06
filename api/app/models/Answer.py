from api.core.storage import Model


class Answer(Model):
    @classmethod
    def by_question_id(cls, qtn_id, ans_id):
        return cls.where(question_id=qtn_id, id=ans_id).first_or_fail()
