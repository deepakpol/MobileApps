class SendPicturePrintTests:
    """Tests for Send picture print and check UI feature"""

    def test_send_picture_print_job(self):
        """
        Test sending a picture print job
        Verifies that a picture can be selected and print job submitted with correct UI
        """
        # TODO: Navigate to mini program home page after launch
        
        # Select picture print category
        self.fc.flow["print_flow"].select_picture_print()
        
        # Select from album
        self.fc.flow["print_flow"].select_from_album()
        
        # Pick a photo (default first photo)
        self.fc.flow["print_flow"].pick_a_photo(index=0)
        
        # Verify print setting page is displayed
        self.fc.flow["print_setting"].verify_print_setting_page()
        
        # Click print button
        self.fc.flow["print_setting"].select_print()
        
        # Verify job submitted message
        self.fc.flow["print_setting"].verify_job_success_submitted_msg()


    def test_send_document_print_job_from_wechat(self):
        """
        Test sending a document print job from WeChat chat history
        Verifies that a document can be selected from chat and print job submitted
        """
        # TODO: Navigate to mini program home page after launch
        # TODO: Ensure test document exists in chat history
        
        # Select file print category
        self.fc.flow["print_flow"].select_file_print()
        
        # Select from chat history option
        self.fc.flow["print_flow"].select_from_chat_history()
        
        # Select a document from chat history
        # TODO: Replace "test_document.pdf" with actual test file name
        self.fc.flow["print_flow"].select_doc_from_chat_history("test_document.pdf")
        
        # Verify print setting page is displayed
        self.fc.flow["print_setting"].verify_print_setting_page()
        
        # Click print button
        self.fc.flow["print_setting"].select_print()
        
        # Verify job submitted message
        self.fc.flow["print_setting"].verify_job_success_submitted_msg()
