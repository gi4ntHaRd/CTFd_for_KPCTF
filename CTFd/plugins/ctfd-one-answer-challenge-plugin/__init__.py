from flask import Blueprint

from CTFd.models import Flags, Solves, db
from CTFd.plugins import register_plugin_assets_directory
from CTFd.plugins.flags import FlagException, get_flag_class
from CTFd.plugins.challenges import CHALLENGE_CLASSES, BaseChallenge

class OneAnswerChallengeModel(db.Model):
    __tablename__ = "one_answer_challenge"
    id = db.Column(db.Integer, db.ForeignKey("challenges.id"), primary_key=True)
    solved_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

class OneAnswerChallengeClass(BaseChallenge):
    id = "one_answer_challenge"
    name = "One Answer Challenge"
    templates = {
        "create": "/plugins/ctfd-one-answer-challenge-plugin/assets/create.html",
        "update": "/plugins/ctfd-one-answer-challenge-plugin/assets/update.html",
        "view": "/plugins/ctfd-one-answer-challenge-plugin/assets/view.html",
    }
    scripts = {
        "create": "/plugins/ctfd-one-answer-challenge-plugin/assets/create.js",
        "update": "/plugins/ctfd-one-answer-challenge-plugin/assets/update.js",
        "view": "/plugins/ctfd-one-answer-challenge-plugin/assets/view.js",
    }
    
    blueprint = Blueprint(
        "one_answer_challenge", __name__,
        template_folder="templates", static_folder="assets"
    )

    @classmethod
    def attempt(cls, challenge, request):
        """
        This method is used to check whether a given input is right or wrong. It does not make any changes and should
        return a boolean for correctness and a string to be shown to the user. It is also in charge of parsing the
        user's input from the request itself.
    
        :param challenge: The Challenge object from the database
        :param request: The request the user submitted
        :param cls_instance: An instance of the challenge class
        :return: (boolean, string)
        """
        data = request.form or request.get_json()
        submission = data["submission"].strip()
    
        # Check if the challenge has already been solved by someone
        existing_solve = (
            Solves.query.filter_by(challenge_id=challenge.id, provided=submission).first()
        )
        if existing_solve:
            return False, "This challenge has already been solved."
    

        flags = Flags.query.filter_by(challenge_id=challenge.id).all()
        for flag in flags:
            try:
                if get_flag_class(flag.type).compare(flag, submission):
                    return True, "Correct"
            except FlagException as e:
                return False, str(e)
        return False, "Incorrect"



def load(app):
    app.register_blueprint(OneAnswerChallengeClass.blueprint)
    CHALLENGE_CLASSES["one_answer_challenge"] = OneAnswerChallengeClass
    register_plugin_assets_directory(
        app, base_path="/plugins/ctfd-one-answer-challenge-plugin/assets/"
    )
